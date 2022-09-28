from jd.api.base import RestApi

class ComJdThPopOpenOrderInformationFacadeListOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sellerSkuId = None
			self.orderCreateTimeBegin = None
			self.pin = None
			self.page = None
			self.paymentType = None
			self.locale = None
			self.skuId = None
			self.pageSize = None
			self.consumerMobilePhone = None
			self.skuName = None
			self.orderStatusType = None
			self.orderId = None
			self.orderCreateTimeEnd = None
			self.open_id_buyer = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderInformationFacade.listOrder'

			




