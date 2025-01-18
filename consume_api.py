import requests
import json 
import pprint

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?fromdate=1733011200&todate=1737072000&order=asc&sort=votes&site=stackoverflow'
)

     
for data in response.json()['items']:
    print('------------------------')    
    
    print(data['title'])
