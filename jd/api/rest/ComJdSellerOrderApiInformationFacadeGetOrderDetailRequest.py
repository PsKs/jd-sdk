from jd.api.base import RestApi

class ComJdSellerOrderApiInformationFacadeGetOrderDetailRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.showTrack = None
			self.language = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.InformationFacade.getOrderDetail'

			




