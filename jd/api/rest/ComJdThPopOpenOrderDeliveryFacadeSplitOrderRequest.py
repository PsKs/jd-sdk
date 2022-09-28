from jd.api.base import RestApi

class ComJdThPopOpenOrderDeliveryFacadeSplitOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.param = None

		def getapiname(self):
			return 'jingdong.com.jd.th.pop.open.OrderDeliveryFacade.splitOrder'

			
	

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
			self.groupId = None
			self.skus = None


class Param(object):
		def __init__(self):
			"""
			"""
			self.desc = None
			self.venderId = None
			self.skuGroup = None
			self.orderId = None




