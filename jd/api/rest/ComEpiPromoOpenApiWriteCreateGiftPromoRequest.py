from jd.api.base import RestApi

class ComEpiPromoOpenApiWriteCreateGiftPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.giftPromoPrice = None
			self.giftSkuId = None
			self.giftQuantity = None
			self.giftProductId = None
			self.giftJdPrice = None
			self.giftSkuName = None
			self.promoPrice = None
			self.skuId = None
			self.quantity = None
			self.productId = None
			self.jdPrice = None
			self.skuName = None
			self.beginTime = None
			self.endTime = None
			self.promoName = None

		def getapiname(self):
			return 'jingdong.com.epi.PromoOpenApiWrite.createGiftPromo'

			




