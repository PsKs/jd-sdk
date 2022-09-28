from jd.api.base import RestApi

class ComEpiPromoOpenApiWriteCreateSuitPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.saveBean = None

		def getapiname(self):
			return 'jingdong.com.epi.PromoOpenApiWrite.createSuitPromo'

			
	

class Attribute2(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.productId = None
			self.promoPrice = None
			self.jdPrice = None
			self.quantity = None
			self.skuName = None


class Attribute1(object):
		def __init__(self):
			"""
			"""
			self.promoSkuBeans = None
			self.discountPrice = None


class SaveBean(object):
		def __init__(self):
			"""
			"""
			self.suitPoolSaveBeans = None
			self.beginTime = None
			self.endTime = None
			self.promoName = None




