import requests
url = r'http://localhost:8080/jenkins/j_acegi_security_check'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
d = {
"from":""
,"j_username":"admin"
,"j_password":"admin"
,"Jenkins-Crumb":"dac408a1bd00ab82173e30bea13aac68"
,"json":{"j_username": "admin", "j_password": "admin", "remember_me": True, "from": "/jenkins/", "Jenkins-Crumb": "dac408a1bd00ab82173e30bea13aac68"}
,'Submit':"登录"
,"remember_me":True}
s = requests.session()
r = s.post(url, headers=headers, data=d)
print(r.text)