from jd.api.base import RestApi

class ThSellerPopSkuBindStoreRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.batchSkuBindStoreApiParam = None

		def getapiname(self):
			return 'jingdong.th.seller.pop.skuBindStore'

			
	

class Attribute2(object):
		def __init__(self):
			"""
			"""
			self.storeSkuStatus = None
			self.storeId = None


class Attribute1(object):
		def __init__(self):
			"""
			"""
			self.skuId = None
			self.storeApiParamList = None


class BatchSkuBindStoreApiParam(object):
		def __init__(self):
			"""
			"""
			self.batchStoreSkuApiParams = None
			self.locale = None




