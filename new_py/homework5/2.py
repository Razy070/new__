import json

import requests

url = 'https://jsonplaceholder.typicode.com/photos'

resp = requests.get(url=url)
data = resp.json()  # Check the JSON Response Content documentation below

with open('txt/data.txt', 'w') as f:
    json.dump(data, f)
