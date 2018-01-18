import requests 
r = requests.get('http://www.cnblogs.com/beard')
# r2 = requests.head('http://www.cnblogs.com/beard')
# print(r.status_code)
# print(r2.status_code)
# print(r.text)
print(r.headers)