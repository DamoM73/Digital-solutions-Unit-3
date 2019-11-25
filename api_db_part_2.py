import requests
import json

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


