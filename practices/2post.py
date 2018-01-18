import requests
import json
payload = {'username':'admin','password':'admin'}
data_json = json.dumps(payload)
r = requests.post('http://192.168.218.117:8081/api/accounts/login/', data = data_json)
print(r.url)
r3 = requests.post('http://httpbin.org/post', data = data_json)
r2 = requests.post('http://httpbin.org/post', data = payload)
print(r.status_code)
print(r.text)
print(r2.text)
print(r3.text)