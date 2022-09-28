from jd.api.base import RestApi

class ComJdGmsGreatdaneCategoryServiceReadCategoryReadServiceGetCategorysRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.categoryIds = None
			self.jarVersion = None
			self.uuid = None
			self.ip = None
			self.hostName = None
			self.instanceHome = None
			self.appId = None
			self.appName = None
			self.sourceIp = None
			self.userAgent = None
			self.businessIdentity = None

		def getapiname(self):
			return 'jingdong.com.jd.gms.greatdane.category.service.read.CategoryReadService.getCategorys'

			




