import requests
import unittest
import sys
sys.path.append('./')
class WDMS():
	def __init__(self,s):
		self.s = s
	def login(self,username,password):
		url = 'http://127.0.0.1:8081/api/accounts/login/'
		payload = {'username':username,'password':password}
		r = self.s.post(url,json = payload)
		return r.json()
	def logout(self,username,password):
		url = 'http://127.0.0.1:8081/api/accounts/logout/'
		payload = {'username':username,'password':password}
		r = self.s.post(url,json = payload)
		return r.json()
	def get_device_info(self,)