from libs.wdms import WDMS
import requests
import unittest
# import json
class zones(unittest.TestCase):
	def setUp(self):
		s = requests.session()
		self.WDMS = WDMS(s)
	#create zone
	def test_create_zone(self):
		'''创建区域'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.create_zone(122,'test')
		self.assertEqual(r['message'],'Succeed')
		self.assertEqual(r['code'],200)
	#update zone
	def test_update_zone(self):
		'''更新区域名称'''
		self.WDMS.login('admin','admin')
		r = self.WDMS.create_zone(122,'test2')
		self.assertEqual(r['message'],'Succeed')
		self.assertEqual(r['code'],200)