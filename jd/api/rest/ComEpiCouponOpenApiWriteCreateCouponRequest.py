from jd.api.base import RestApi

class ComEpiCouponOpenApiWriteCreateCouponRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.createCouponWay = None
			self.wareIdList = None
			self.collectionTimeBegin = None
			self.couponType = None
			self.collectionTimeEnd = None
			self.validityType = None
			self.thName = None
			self.usName = None
			self.reonly = None
			self.validityTimeEnd = None
			self.discountOff = None
			self.display = None
			self.discountOffValid = None
			self.takeRule = None
			self.activityLink = None
			self.discount = None
			self.validityTimeBegin = None
			self.num = None
			self.quota = None
			self.discountOffMax = None

		def getapiname(self):
			return 'jingdong.com.epi.couponOpenApiWrite.createCoupon'

			




