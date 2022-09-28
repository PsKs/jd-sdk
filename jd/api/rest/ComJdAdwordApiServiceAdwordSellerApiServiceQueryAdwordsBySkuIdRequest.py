from jd.api.base import RestApi

class ComJdAdwordApiServiceAdwordSellerApiServiceQueryAdwordsBySkuIdRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuId = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.jd.adword.api.service.AdwordSellerApiService.queryAdwordsBySkuId'

			




