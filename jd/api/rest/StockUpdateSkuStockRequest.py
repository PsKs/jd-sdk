from jd.api.base import RestApi

class StockUpdateSkuStockRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sid = None
			self.stockNum = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.stock.updateSkuStock'

			




