import requests
url = 'http://localhost:5000/events'
data = '{  "name": "sample" }'
response = requests.post(url, data=data,headers={"Content-Type": "application/json"})
print(response)
sid=response.json()['id']
print(response.text)
print(sid)

response = requests.get(url)
events = response.json()
print (events)

response = requests.delete(url + '/' + sid)
print(response)