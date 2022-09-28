from jd.api.base import RestApi

class ComEpiPromoOpenApiReadGetPromoMainSkuRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promoId = None
			self.attribute1 = None
			self.deleteState = None
			self.pageSize = None
			self.skuId = None
			self.promoType = None
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.com.epi.promoOpenApiRead.getPromoMainSku'

			




