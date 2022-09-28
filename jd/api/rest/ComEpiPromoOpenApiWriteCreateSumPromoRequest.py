from jd.api.base import RestApi

class ComEpiPromoOpenApiWriteCreateSumPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.favorMode = None
			self.promoPrice = None
			self.skuId = None
			self.skuName = None
			self.jdPrice = None
			self.quantity = None
			self.productId = None
			self.beginTime = None
			self.endTime = None
			self.promoName = None
			self.quota = None
			self.rate = None

		def getapiname(self):
			return 'jingdong.com.epi.PromoOpenApiWrite.createSumPromo'

			




