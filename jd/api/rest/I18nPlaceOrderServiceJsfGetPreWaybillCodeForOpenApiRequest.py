from jd.api.base import RestApi

class I18nPlaceOrderServiceJsfGetPreWaybillCodeForOpenApiRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.venderId = None
			self.outSource = None
			self.source = None
			self.orderType = None
			self.customerCode = None
			self.orderId = None
			self.countryFlag = None
			self.siteFlag = None

		def getapiname(self):
			return 'jingdong.i18n.PlaceOrderServiceJsf.getPreWaybillCodeForOpenApi'

			




