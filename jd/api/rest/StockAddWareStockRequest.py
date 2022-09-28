from jd.api.base import RestApi

class StockAddWareStockRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sid = None
			self.skuId = None

		def getapiname(self):
			return 'jingdong.stock.addWareStock'

			




