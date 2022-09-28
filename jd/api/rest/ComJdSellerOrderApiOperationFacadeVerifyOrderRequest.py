from jd.api.base import RestApi

class ComJdSellerOrderApiOperationFacadeVerifyOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.language = None
			self.orderId = None
			self.verifyCode = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.OperationFacade.verifyOrder'

			




