from jd.api.base import RestApi

class ComJdIntlAsmShopAfsApiServiceQueryDetailRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.language = None
			self.serviceId = None

		def getapiname(self):
			return 'jingdong.com.jd.intl.asm.shop.AfsApiService.queryDetail'

			




