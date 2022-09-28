from jd.api.base import RestApi

class JosVoucherInfoGetRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customer_user_id = None
			self.access_token = None

		def getapiname(self):
			return 'jingdong.jos.voucher.info.get'

			




