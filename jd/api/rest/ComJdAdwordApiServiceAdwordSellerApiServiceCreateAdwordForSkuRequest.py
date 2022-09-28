from jd.api.base import RestApi

class ComJdAdwordApiServiceAdwordSellerApiServiceCreateAdwordForSkuRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.pcLink = None
			self.adwordContent = None
			self.advanced = None
			self.skuId = None
			self.beginTime = None
			self.language = None
			self.appLink = None
			self.linkName = None
			self.stopTime = None
			self.productId = None

		def getapiname(self):
			return 'jingdong.com.jd.adword.api.service.AdwordSellerApiService.createAdwordForSku'

			




