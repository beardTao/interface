import requests
url1 = r'http://192.168.218.117:8081/api/accounts/login/'
url2 = r'http://192.168.218.117:8081/api/accounts/logout/'
payload1 = {
'username':'admin'
,'password':'admin'
}
payload2 = {
'username':'admin'
,'password':'admin'
}
s = requests.session()
r1 = s.post(url1,json = payload1)
r2 = s.post(url2,json = payload2)
print(r1.status_code)
print(r1.text)
print(r2.status_code)
print(r2.text)