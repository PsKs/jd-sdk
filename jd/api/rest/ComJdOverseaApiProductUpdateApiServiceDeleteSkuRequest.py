from jd.api.base import RestApi

class ComJdOverseaApiProductUpdateApiServiceDeleteSkuRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.locale = None

		def getapiname(self):
			return 'jingdong.com.jd.oversea.api.ProductUpdateApiService.deleteSku'

			




