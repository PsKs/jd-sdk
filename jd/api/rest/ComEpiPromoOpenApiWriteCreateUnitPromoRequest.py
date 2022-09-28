from jd.api.base import RestApi

class ComEpiPromoOpenApiWriteCreateUnitPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.token = None
			self.perMaxNum = None
			self.promoPrice = None
			self.skuId = None
			self.quantity = None
			self.productId = None
			self.jdPrice = None
			self.skuName = None
			self.beginTime = None
			self.freqBound = None
			self.endTime = None
			self.promoName = None
			self.perMinNum = None

		def getapiname(self):
			return 'jingdong.com.epi.PromoOpenApiWrite.createUnitPromo'

			




