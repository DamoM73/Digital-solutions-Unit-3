import requests
import json

# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

# check request status
print(trucks_data.status_code)

# view data 
print(trucks_data.json())

