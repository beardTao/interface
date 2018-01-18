import requests
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
s = requests.session()
r = s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',headers = headers,allow_redirects=False,verify = False)
new_url = r.headers["Location"]
print(r.status_code)
print(new_url)