from jd.api.base import RestApi

class ComProductUpdateApiServiceChangeSkuStatusRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.status = None
			self.locale = None
			self.skuId = None
			self.productId = None

		def getapiname(self):
			return 'jingdong.com.productUpdateApiService.changeSkuStatus'

			




