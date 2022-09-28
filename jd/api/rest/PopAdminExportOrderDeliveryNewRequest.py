from jd.api.base import RestApi

class PopAdminExportOrderDeliveryNewRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.logisticsNo = None
			self.logisticsId = None
			self.pickUpAddress = None
			self.logisticsCompany = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.PopAdminExport.orderDeliveryNew'

			




