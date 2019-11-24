import requests
import json
import sqlite3

def create_table(filename, tablename, sqlcommand):
    # connect to database file (will create it if not existing)
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()

    # remove previous table and data
    cursor.execute(f"DROP TABLE IF EXISTS {tablename}")

    # create empty table
    cursor.execute(sqlcommand)

def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retrieval not successful, diplay error number
    else:
        print(obj.status_code, "error in retrieving API")

# ---- MAIN PROGRAM ----
# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

# display formatted data
jprint(trucks_data)


