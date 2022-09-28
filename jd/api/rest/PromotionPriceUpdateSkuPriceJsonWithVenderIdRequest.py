from jd.api.base import RestApi

class PromotionPriceUpdateSkuPriceJsonWithVenderIdRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.wid = None
			self.salePriceBefore = None
			self.salePrice = None
			self.appReason = None
			self.applicant = None
			self.reviewer = None
			self.auditReason = None

		def getapiname(self):
			return 'jingdong.promotion.price.updateSkuPriceJsonWithVenderId'

			




