from jd.api.base import RestApi

class ComJdSellerOrderApiOperationFacadeAcceptOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.acceptType = None
			self.language = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.OperationFacade.acceptOrder'

			




