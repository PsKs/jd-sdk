from jd.api.base import RestApi

class ComProductQueryApiServiceQueryProductsRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.locale = None
			self.skuId = None
			self.secondCategory = None
			self.yn = None
			self.saleState = None
			self.thirdCategory = None
			self.firstCategory = None
			self.brandId = None
			self.productName = None
			self.outerId = None
			self.pageNum = None
			self.productId = None
			self.myriad = None

		def getapiname(self):
			return 'jingdong.com.productQueryApiService.queryProducts'

			




