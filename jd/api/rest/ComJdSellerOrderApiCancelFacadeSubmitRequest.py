from jd.api.base import RestApi

class ComJdSellerOrderApiCancelFacadeSubmitRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.reasonType = None
			self.reasonCode = None
			self.language = None
			self.orderId = None
			self.reasonDesc = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.CancelFacade.submit'

			




