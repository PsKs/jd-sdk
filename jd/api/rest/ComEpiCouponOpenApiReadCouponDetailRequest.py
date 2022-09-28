from jd.api.base import RestApi

class ComEpiCouponOpenApiReadCouponDetailRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.couponId = None

		def getapiname(self):
			return 'jingdong.com.epi.couponOpenApiRead.couponDetail'

			




