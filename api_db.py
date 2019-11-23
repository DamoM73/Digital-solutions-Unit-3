import requests
import json
import sqlite3

DB_FILE = "food_trucks.db"

def create_table(filename, tablename, sqlcommand):
    # connect to database file (will create it if not existing)
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()

        # remove previous table and data
        cursor.execute(f"DROP TABLE IF EXISTS {tablename};")

        # create empty table
        cursor.execute(sqlcommand)

def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retrieval not successful, diplay error number
    else:
        print(obj.status_code, "error in retrieving API")

def table_insert(db_file, table_name, data):
    # connect to database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        for row in data:
            truck_id = row['truck_id']
            name = row['name']
            category = row['category']
            if row['website'] == '':
                website = 'none'
            else:
                website = row['website']
            values = f'{truck_id}, "{name}", "{category}", "{website}"'
            print(values)

            cursor.execute(f"""
                            INSERT INTO {table_name}
                            VALUES ({values});
                            """)

# ---- MAIN PROGRAM ----
# retrieve data from API
trucks_response = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

# display formatted data
#jprint(trucks_response)

# create database tables
create_truck_tbl = """
                    CREATE TABLE Trucks (
	                    truck_id INTEGER PRIMARY KEY,
	                    name TEXT NOT NULL,
	                    category TEXT NOT NULL,
	                    website TEXT);
                    """

create_table(DB_FILE,"Trucks",create_truck_tbl)

# write data from JSON file to database
table_insert(DB_FILE,"Trucks", trucks_response.json())
    