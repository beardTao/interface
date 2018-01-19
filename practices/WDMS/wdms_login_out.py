import requests
url = r'http://192.168.218.117:8081/api/accounts/logout/'
headers = {
'Cookie': 'tointerval=30; toenable=false; _fw=COL0%099%09SN%09152%09Alias%09116%09COL3%0938%09LastActivity%0977%09FWVersion%0998%09DeviceName%0985%09UserCount%0967%09FPCount%0952%09FaceCount%0967%09TransactionCount%09113%09PvCount%0969%09COL12%0961%09COL13%0927%09DeptID%09124%09company%0928; csrftoken=dbd969ffcde2d4905995ee1e3bb5b70b; sessionid=e5337af3f9d6a704f92f8c80c01679cc'
}
payload = {
'username':'admin'
,'password':'admin'
}
r = requests.post(url,headers = headers,json = payload)
print(r.status_code)
print(r.text)