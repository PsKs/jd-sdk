from jd.api.base import RestApi

class ComJdThPopOpenOrderCancelFacadeSubmitCancelOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.locale = None
			self.reasonCode = None
			self.orderId = None
			self.reasonDesc = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderCancelFacade.submitCancelOrder'

			




