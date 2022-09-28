from jd.api.base import RestApi

class ComJdOverseaApiProductUpdateApiServiceRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.productId = None
			self.locale = None

		def getapiname(self):
			return 'jingdong.com.jd.oversea.api.ProductUpdateApiService'

			




