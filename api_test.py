import urllib3

url = 'https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=18ee2911-992f-40ed-b6ae-e756859786e6&limit=5&q=title:jones'
fileobj = urllib3.urlopen(url)
