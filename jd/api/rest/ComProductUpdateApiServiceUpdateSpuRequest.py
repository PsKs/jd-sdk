from jd.api.base import RestApi

class ComProductUpdateApiServiceUpdateSpuRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.updateSpuApiParam = None

		def getapiname(self):
			return 'jingdong.com.productUpdateApiService.updateSpu'

			
	

class UpdateSpuApiParam(object):
		def __init__(self):
			"""
			"""
			self.afterSales = None
			self.canUseDQ = None
			self.sn = None
			self.wareQD = None
			self.payFirst = None
			self.locale = None
			self.thName = None
			self.categoryAttrs = None
			self.shopCategory = None
			self.canUseJQ = None
			self.brandId = None
			self.productId = None
			self.templateId = None
			self.shelfLife = None
			self.unit = None
			self.enName = None
			self.promiseId = None
			self.pcDescription = None
			self.is15ToReturn = None
			self.warranty = None
			self.appDescription = None




