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

def table_insert(db_file, table_name, values):
    # connect to database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()
        
        # execute an insert statement for each row of provided data list
        records = 0
        for row in values:
            #print(row)
            cursor.execute(f"""
                            INSERT INTO {table_name}
                            VALUES ({row});
                            """)
            records += 1
        print(f"Added {records} records to the {table_name} table")

def sql_query(db_file, query):
    # connect with database file
    with sqlite3.connect(db_file) as database:
        cursor = database.cursor()

        # execute provided query
        cursor.execute(query)
        return cursor.fetchall()


# ---- MAIN PROGRAM ----
# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")
sites_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/sites")
bookings_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")

# display formatted data
#jprint(sites_data)

# -- create database tables --
# truck table
create_truck_tbl = """
                    CREATE TABLE Trucks (
	                    truck_id INTEGER PRIMARY KEY,
	                    name TEXT NOT NULL,
	                    category TEXT NOT NULL,
	                    website TEXT);
                    """
create_table(DB_FILE,"Trucks",create_truck_tbl)

# sites table
create_sites_tbl = """
                    CREATE TABLE Sites (
	                    site_id INTEGER PRIMARY KEY,
	                    street TEXT NOT NULL,
	                    suburb TEXT NOT NULL,
	                    postcode INTEGER NOT NULL,
	                    latitude REAL,
	                    longitude REAL);
                    """
create_table(DB_FILE,"Sites",create_sites_tbl)

# bookings table
create_bookings_tble = """
                        CREATE TABLE Bookings (
                            	booking_id INTEGER PRIMARY KEY,
                                site_id INTEGER NOT NULL,
                                truck_id INTEGER NOT NULL,
                                date TEXT, 
                                start TEXT,
                                finish TEXT);
                        """
create_table(DB_FILE,"Bookings",create_bookings_tble)

# -- write data from JSON files to database --
# create a list with an element for each row of the json file

# truck table
values = []
for row in trucks_data.json():
    truck_id = row['truck_id']
    name = row['name']
    category = row['category']
    if row['website'] == '':
        website = 'none'
    else:
        website = row['website']
    values.append(f'{truck_id}, "{name}", "{category}", "{website}"')
table_insert(DB_FILE,"Trucks", values)

# sites table
values = []
for row in sites_data.json():
    site_id = row['site_id']
    street = row['street']
    suburb = row['suburb']
    postcode = row['postcode']
    latitude = row['latitude']
    longitude = row['longitude']
    values.append(f'{site_id}, "{street}", "{suburb}", "{postcode}", "{latitude}", "{longitude}" ')
table_insert(DB_FILE,"Sites", values)

# bookings table
values = []
for row in bookings_data.json():
    booking_id = row['start'][:4]+row['start'][5:7]+row['start'][8:10]+row['site_id']+row['truck_id']
    site_id = row['site_id']
    truck_id = row['truck_id']
    date = row['start'][8:10] + "-" + row['start'][5:7] + "-" + row['start'][:4]
    start = row['start'][11:16]
    finish = row['finish'][11:16]
    values.append(f'{booking_id}, {site_id}, {truck_id}, "{date}", "{start}", "{finish}"')
table_insert(DB_FILE,"Bookings", values)

# -- query to produce table
create_listing = """
                    SELECT Bookings.date, Bookings.start, Trucks.name, Sites.street, Sites.suburb
                    FROM Bookings
                    JOIN Trucks
                    ON Bookings.truck_id = Trucks.truck_id
                    JOIN Sites
                    ON Bookings.site_id = Sites.site_id
                    ORDER BY Bookings.date
                """

listing = sql_query(DB_FILE,create_listing)

for row in listing:
    print(row)
