from jd.api.base import RestApi

class ComProductQueryApiServiceQuerySkusByOuterIdsRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.locale = None
			self.sellerSkuIds = None

		def getapiname(self):
			return 'jingdong.com.productQueryApiService.querySkusByOuterIds'

			




