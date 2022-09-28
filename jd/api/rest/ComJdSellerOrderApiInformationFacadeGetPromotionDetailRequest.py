from jd.api.base import RestApi

class ComJdSellerOrderApiInformationFacadeGetPromotionDetailRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.language = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.InformationFacade.getPromotionDetail'

			




