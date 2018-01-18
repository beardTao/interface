import requests
import unittest
import json
# url = r'http://127.0.0.1:8081/api/accounts/login/'
# payload = {
# 'username':'admin'
# ,'password':'admin'
# }
# r1 = requests.post(url1,json = payload)
# print(r1.status_code)
# print(r1.text)
class Login_test(unittest.TestCase):
	def setUp(self):
		self.url = r'http://127.0.0.1:8081/api/accounts/login/'
	def test_login_successful(self):
		payload = {'username':'admin','password':'admin'}
		self.r = requests.post(self.url, json = payload)
		res = self.r.json()
		result_message = res['message']
		result_code = res['code']
		hope_code = 200
		hope_meaasge = 'Login Successful'
		self.assertEqual(result_message,hope_meaasge)
		self.assertEqual(result_code,hope_code)
	def test_login_fail1(self):
		payload = {'username':'admin1','password':'admin'}
		self.r = requests.post(self.url, json = payload)
		res = self.r.json()
		result_message = res['message']
		result_code = res['code']
		hope_code = 1002
		hope_meaasge = 'Username Or Password Is Incorrect'
		self.assertEqual(result_message,hope_meaasge)
		self.assertEqual(result_code,hope_code)
	def test_login_fail2(self):
		payload = {'username':'admin','password':'admin1'}
		self.r = requests.post(self.url, json = payload)
		res = self.r.json()
		result_message = res['message']
		result_code = res['code']
		hope_code = 1002
		hope_meaasge = 'Username Or Password Is Incorrect'
		self.assertEqual(result_message,hope_meaasge)
		self.assertEqual(result_code,hope_code)
	def tearDown(self):
		self.r.close()
if __name__ == '__main__':
	unittest.main()