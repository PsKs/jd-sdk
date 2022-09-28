from jd.api.base import RestApi

class ThSellerPopSearchStoreSkuListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.page = None
			self.pageSize = None
			self.locale = None
			self.skuId = None
			self.categoryId = None
			self.brandId = None
			self.skuName = None
			self.shopCategoryIds = None
			self.status = None
			self.storeIdList = None

		def getapiname(self):
			return 'jingdong.th.seller.pop.searchStoreSkuList'

			




