import unittest
import requests
import HTMLTestRunner
class WDMS_login(unittest.TestCase):
	def login(self,username,password):
		url = 'http://127.0.0.1:8081/api/accounts/login/'
		payload = {'username':username,'password':password}
		self.r = requests.post(url,json = payload)
	def test_login_successful(self):
		self.login('admin','admin')
		print(self.r.json())
		self.assertEqual('Login Successful',self.r.json()['message'])
	def test_login_defeat(self):
		self.login('admin','admin1')
		print(self.r.json())
		self.assertEqual('Username Or Password Is Incorrect',self.r.json()['message'])
		self.assertEqual(1002,self.r.json()['code'])
if __name__ == '__main__':
	unittest.main()