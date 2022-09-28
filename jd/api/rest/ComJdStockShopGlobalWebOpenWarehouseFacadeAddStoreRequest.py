from jd.api.base import RestApi

class ComJdStockShopGlobalWebOpenWarehouseFacadeAddStoreRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.storeName = None
			self.remark = None
			self.venderId = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.com.jd.stock.shop.global.web.open.WarehouseFacade.addStore'

			




