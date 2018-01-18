import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = r'http://192.168.214.219:8088/login.jsp'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
"Accept": "application/json, text/javascript, */*; q=0.01",
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length':'142'
,'Cookie': 'clientHeight=690; clientWidth=1525; JSESSIONID=A4155C04E5385BF4FE02AB1BEAD8DAA0; backUrl=/base_index.action; eMsgIsColse=true; leftMenuId/base_index.action=auth_listAuthUser.action; leftMenuId/acc_index.action=iframe:acc_listAccRTMonitor.action?type=custom; leftMenuId/pers_index.action=pers_listPersPerson.action?type=custom'
,'Connection': 'keep-alive'}
payload = {
'username':'tao'
,'password':'admin'
,'loginType':'NORMAL'
,'autoLogin':'1'
,'un':'1515122815340_3135'
,'systemCode':'login.jsp'
,'un':'1515122815343_2671'
,'systemCode':'login.jsp'
}
s = requests.session()
r = s.post(url, headers=headers, data=payload)
print(r.encoding)
print(r.content)