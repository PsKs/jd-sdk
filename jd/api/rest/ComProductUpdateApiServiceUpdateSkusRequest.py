from jd.api.base import RestApi

class ComProductUpdateApiServiceUpdateSkusRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.updateSkuApiParam = None

		def getapiname(self):
			return 'jingdong.com.productUpdateApiService.updateSkus'

			
	

class CategoryAttributeValueParam(object):
		def __init__(self):
			"""
			"""
			self.id = None
			self.dimension = None
			self.orderSort = None
			self.comAttId = None
			self.required = None
			self.localeName = None


class SkuApiParam(object):
		def __init__(self):
			"""
			"""
			self.weight = None
			self.stockNum = None
			self.productCode = None
			self.width = None
			self.jdPrice = None
			self.height = None
			self.saleAttrs = None
			self.skuStatus = None
			self.upcCode = None
			self.skuId = None
			self.length = None
			self.outerId = None


class StockParam(object):
		def __init__(self):
			"""
			"""
			self.warehouseId = None
			self.updateStockNum = None


class ImageParam(object):
		def __init__(self):
			"""
			"""
			self.imgUrl = None
			self.index = None
			self.colorId = None


class UpdateSkuApiParam(object):
		def __init__(self):
			"""
			"""
			self.locale = None
			self.skuList = None
			self.updateSkuStockMap = None
			self.imageMap = None
			self.productId = None




