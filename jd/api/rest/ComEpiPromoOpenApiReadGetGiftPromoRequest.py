from jd.api.base import RestApi

class ComEpiPromoOpenApiReadGetGiftPromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promoId = None

		def getapiname(self):
			return 'jingdong.com.epi.promoOpenApiRead.getGiftPromo'

			




