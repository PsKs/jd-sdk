from jd.api.base import RestApi

class ComJdSellerOrderApiCancelFacadeReviewRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.id = None
			self.remark = None
			self.status = None
			self.outWareStatus = None
			self.rejectType = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.CancelFacade.review'

			




