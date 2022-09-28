from jd.api.base import RestApi

class ComJdThPopOpenOrderPrintFacadePrintLabelRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderIds = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderPrintFacade.printLabel'

			




