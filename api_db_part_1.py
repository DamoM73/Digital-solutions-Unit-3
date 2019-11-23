import requests
import json

# retrieve data from API
trucks_response = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")

# check request status
print(trucks_response.status_code)

# view data 
print(trucks_response.json())

