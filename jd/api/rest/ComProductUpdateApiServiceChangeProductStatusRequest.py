from jd.api.base import RestApi

class ComProductUpdateApiServiceChangeProductStatusRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.status = None
			self.locale = None
			self.productId = None

		def getapiname(self):
			return 'jingdong.com.productUpdateApiService.changeProductStatus'

			




