from jd.api.base import RestApi

class ComJdSellerOrderApiDeliveryFacadeDeliveryRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.logisticsNo = None
			self.logisticsId = None
			self.logisticsCompany = None
			self.language = None
			self.serviceType = None
			self.addressId = None
			self.orderId = None
			self.deliveryType = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.DeliveryFacade.delivery'

			




