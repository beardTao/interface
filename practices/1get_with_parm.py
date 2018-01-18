import requests 
loc = r'http://zzk.cnblogs.com/s/blogpost'
par = {'Keywords':'上海-悠悠'}
r = requests.get(loc,params = par)
print(r.status_code)
print(r.text)