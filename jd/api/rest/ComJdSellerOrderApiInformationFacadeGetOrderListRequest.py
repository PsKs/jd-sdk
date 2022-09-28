from jd.api.base import RestApi

class ComJdSellerOrderApiInformationFacadeGetOrderListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customerName = None
			self.sellerSkuId = None
			self.phone = None
			self.orderBy = None
			self.orderType = None
			self.paymentType = None
			self.language = None
			self.pageSize = None
			self.pageStart = None
			self.unPrintType = None
			self.endTime = None
			self.period = None
			self.startTime = None
			self.sortType = None
			self.skuId = None
			self.orderId = None
			self.tabStatus = None
			self.modifyTimeBegin = None
			self.modifyTimeEnd = None
			self.deliveryType = None
			self.deliveryStatus = None
			self.storeIds = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.InformationFacade.getOrderList'

			




