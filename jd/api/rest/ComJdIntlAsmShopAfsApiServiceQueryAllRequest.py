from jd.api.base import RestApi

class ComJdIntlAsmShopAfsApiServiceQueryAllRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.processResult = None
			self.contactTel = None
			self.auditDateBegin = None
			self.customerPin = None
			self.orderId = None
			self.status = None
			self.pageSize = None
			self.sku = None
			self.auditResult = None
			self.pageIndex = None
			self.serviceId = None
			self.applyTimeBegin = None
			self.applyTimeEnd = None
			self.auditDateEnd = None
			self.language = None
			self.branchId = None

		def getapiname(self):
			return 'jingdong.com.jd.intl.asm.shop.AfsApiService.queryAll'

			




