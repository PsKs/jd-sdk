from jd.api.base import RestApi

class ComProductUpdateApiServiceSaveProductRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.updateProductParam = None

		def getapiname(self):
			return 'jingdong.com.productUpdateApiService.saveProduct'

			
	

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


class ImageParam(object):
		def __init__(self):
			"""
			"""
			self.imgUrl = None
			self.index = None
			self.colorId = None


class StockParam(object):
		def __init__(self):
			"""
			"""
			self.warehouseId = None
			self.updateStockNum = None


class UpdateProductParam(object):
		def __init__(self):
			"""
			"""
			self.afterSales = None
			self.payFirst = None
			self.locale = None
			self.vat = None
			self.categoryAttrs = None
			self.brandId = None
			self.canUseJQ = None
			self.enName = None
			self.promiseId = None
			self.pcDescription = None
			self.countryOfOrigin = None
			self.sn = None
			self.canUseDQ = None
			self.wareQD = None
			self.thName = None
			self.categoryId = None
			self.skuList = None
			self.shopCategory = None
			self.putShelf = None
			self.productId = None
			self.templateId = None
			self.unit = None
			self.shelfLife = None
			self.imageList = None
			self.updateSkuStockMap = None
			self.is15ToReturn = None
			self.warranty = None
			self.appDescription = None




