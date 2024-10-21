'''
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/funnyname/random?n=3' \
  -H 'accept: application/json'
'''
import requests
url = "https://cent.ischool-iot.net/api/funnyname/random"
querystring = {"n":"3"}
# what goes in is different each time
response = requests.get(url, params = querystring)
response.raise_for_status()
names=response.json()
# what comes out is different each time
for name in names:
    print(name['first'], name['last'])



url = "https://cent.ischool-iot.net/api/funnyname/search"
params = {"q":"Mi"}
response = requests.get(url, params = params)
response.raise_for_status()
names = response.json()
for name in names:
    print(name['first'], name['last'])