from jd.api.base import RestApi

class ComEpiPromoOpenApiReadGetPromoListForPageRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promoId = None
			self.skuId = None
			self.sellerSkuId = None
			self.promoType = None
			self.promoState = None
			self.timeBegin = None
			self.timeEnd = None
			self.pageSize = None
			self.pageIndex = None

		def getapiname(self):
			return 'jingdong.com.epi.promoOpenApiRead.getPromoListForPage'

			




