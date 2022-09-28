from jd.api.base import RestApi

class ComProductQueryApiServiceQueryskusRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.locale = None
			self.skuId = None
			self.saleState = None
			self.outerId = None
			self.productId = None

		def getapiname(self):
			return 'jingdong.com.productQueryApiService.queryskus'

			




