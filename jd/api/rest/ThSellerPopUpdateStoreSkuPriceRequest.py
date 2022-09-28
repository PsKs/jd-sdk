from jd.api.base import RestApi

class ThSellerPopUpdateStoreSkuPriceRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.locale = None
			self.skuId = None
			self.storeSkuPrice = None
			self.storeId = None

		def getapiname(self):
			return 'jingdong.th.seller.pop.updateStoreSkuPrice'

			




