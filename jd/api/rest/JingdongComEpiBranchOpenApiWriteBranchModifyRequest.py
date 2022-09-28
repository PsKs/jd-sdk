from jd.api.base import RestApi

class JingdongComEpiBranchOpenApiWriteBranchModifyRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.branchId = None
			self.branchName = None
			self.provinceId = None
			self.cityId = None
			self.countryId = None
			self.provinceName = None
			self.cityName = None
			self.countryName = None
			self.detailAddress = None
			self.lng = None
			self.lat = None
			self.phoneNumber = None
			self.serviceHotline = None
			self.openedTime = None
			self.closedTime = None
			self.branchLogo = None
			self.attribute = None
			self.advertising = None
			self.pickUpType = None
			self.deliveryRightNowType = None
			self.attribute1 = None
			self.agingType = None
			self.preparedTime = None
			self.subscribeTimeType = None
			self.subscribeTime = None
			self.deliveryRangeType = None
			self.lngAttr = None
			self.latAttr = None
			self.minimumDeliveryPrice = None
			self.weightLimit = None
			self.templateId = None
			self.freeShippingType = None
			self.basicDeliveryPrice = None
			self.distance = None
			self.amount = None
			self.weight = None
			self.weightAmount = None
			self.startTime = None
			self.endTime = None
			self.timeAmount = None
			self.language = None

		def getapiname(self):
			return 'jingdong.jingdong.com.epi.branchOpenApiWrite.branchModify'

			




