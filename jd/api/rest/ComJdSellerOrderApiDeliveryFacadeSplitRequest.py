from jd.api.base import RestApi

class ComJdSellerOrderApiDeliveryFacadeSplitRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.param1 = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.order.api.DeliveryFacade.split'

			
	

class Attribute2(object):
		def __init__(self):
			"""
			"""
			self.id = None
			self.num = None
			self.uuid = None


class Attribute1(object):
		def __init__(self):
			"""
			"""
			self.skuDetailList = None


class Param1(object):
		def __init__(self):
			"""
			"""
			self.desc = None
			self.venderId = None
			self.language = None
			self.orderId = None
			self.skuGroups = None




