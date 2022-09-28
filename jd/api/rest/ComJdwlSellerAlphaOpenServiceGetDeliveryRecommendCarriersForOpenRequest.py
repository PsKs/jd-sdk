from jd.api.base import RestApi

class ComJdwlSellerAlphaOpenServiceGetDeliveryRecommendCarriersForOpenRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.sendProvinceId = None
			self.locale = None
			self.clientBUId = None
			self.receiveProvinceId = None
			self.receiveTownId = None
			self.sendCountyId = None
			self.area = None
			self.sendTownId = None
			self.sendCityId = None
			self.skus = None
			self.receiveCityId = None
			self.timezoneId = None
			self.orderId = None
			self.receiveCountyId = None

		def getapiname(self):
			return 'jingdong.com.jdwl.seller.AlphaOpenService.getDeliveryRecommendCarriersForOpen'

			




