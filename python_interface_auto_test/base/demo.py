import requests
import json
class RunMain():

	def send_get(self,url,data):
		res = requests.get(url=url,data=data)
		return res
		
	def send_post(self,url,data):
		res = requests.post(url=url,data=data).json()
		return res

	def run_main(self,url,method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url,data)
		else:
			res = self.send_post(url,data)
		return res

if __name__ == '__main__':
	url = 'https://www.imooc.com'
	data = {
		 'c':'wff'
	}
	runmain = RunMain()
	res = runmain.run_main(url,'GET',data)
	print res
	#print run.run_main(url,'GET',data)
