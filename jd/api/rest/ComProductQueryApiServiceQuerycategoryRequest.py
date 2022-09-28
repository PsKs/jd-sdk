from jd.api.base import RestApi

class ComProductQueryApiServiceQuerycategoryRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.categoryId = None
			self.locale = None

		def getapiname(self):
			return 'jingdong.com.productQueryApiService.querycategory'

			




