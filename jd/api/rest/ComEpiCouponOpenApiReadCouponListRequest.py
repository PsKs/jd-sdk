from jd.api.base import RestApi

class ComEpiCouponOpenApiReadCouponListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.bindType = None
			self.pageSize = None
			self.couponTitle = None
			self.beginTime = None
			self.language = None
			self.endTime = None
			self.deleteStatus = None
			self.pageNum = None

		def getapiname(self):
			return 'jingdong.com.epi.couponOpenApiRead.couponList'

			




