from jd.api.base import RestApi

class ComEpiPromoOpenApiWriteResumePromoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.promoId = None
			self.promoType = None

		def getapiname(self):
			return 'jingdong.com.epi.PromoOpenApiWrite.resumePromo'

			




