import requests
import json
import sqlite3

def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retrieval not successful, diplay error number
    else:
        print(obj.status_code, "error in retrieving API")


# ---- MAIN PROGRAM ----
# retrieve data from API
bookings_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")

# display formatted data
jprint(bookings_data)

for row in bookings_data.json():
    #print(row["start"][:4])
    #print(row["start"][5:7])
    #print(row["start"][8:10])


