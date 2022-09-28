from jd.api.base import RestApi

class PopAdminExportQueryListNewRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.phone = None
			self.pin = None
			self.paymentType = None
			self.originStatuList = None
			self.beginTime = None
			self.yn = None
			self.endTime = None
			self.orderStatus = None
			self.orderId = None
			self.pageSize = None
			self.pageStart = None

		def getapiname(self):
			return 'jingdong.PopAdminExport.queryListNew'

			




