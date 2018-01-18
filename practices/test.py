import requests
r = requests.get('http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html')
print(r.status_code)
print(r.content)