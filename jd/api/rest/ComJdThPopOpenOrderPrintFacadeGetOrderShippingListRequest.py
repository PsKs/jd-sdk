from jd.api.base import RestApi

class ComJdThPopOpenOrderPrintFacadeGetOrderShippingListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.paperType = None
			self.locale = None
			self.md5Sign = None
			self.orderIds = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderPrintFacade.getOrderShippingList'

			




