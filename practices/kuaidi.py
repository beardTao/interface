import requests
import unittest
# import json
import HTMLTestRunner
class Test_kuaidi(unittest.TestCase):
	def setUp(self):
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
	def ckd(self,danhao,kd,kd_name):
		self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html'%(danhao,kd)
		r = requests.get(self.url,headers = self.headers,verify = False)
		#获取返回json值
		result = r.json()
		#获取快递公司名称
		company = result['company']
		#获取data数值
		data = result['data']
		#判断快递公司是否正确
		self.assertEqual(kd_name,company)
		#判断最新签收信息，是否已经签收
		self.assertIn('已签收',data[0]['context'])
	def test_yunda(self):
		'''韵达快递'''
		danhao = '1202247993797'
		kd = 'yunda'
		kd_name = '韵达快递'
		self.ckd(danhao,kd,kd_name)
	def test_shunfeng(self):
		'''顺丰快递'''
		danhao = '789467520541'
		kd = 'shunfeng'
		kd_name = '顺丰快递'
		self.ckd(danhao,kd,kd_name)
if __name__ == '__main__':
	#报告保存路径
	report_dir = r'./report/result.html'
	test_suite = unittest.TestSuite()
	test_suite.addTest(Test_kuaidi('test_yunda'))
	test_suite.addTest(Test_kuaidi('test_shunfeng'))
	with open(report_dir,'wb') as f:
		runner = HTMLTestRunner.HTMLTestRunner(stream = f,title = '快递接口测试报告',description = 'win7')
		runner.run(test_suite)