from jd.api.base import RestApi

class ComJdThPopOpenOrderInformationFacadeQueryPaymentDetailInfoRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.locale = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderInformationFacade.queryPaymentDetailInfo'

			




