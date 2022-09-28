from jd.api.base import RestApi

class ComJdAddressInternationalGlscGlscAddressCodingServiceWSParseAddressCodingRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.locale = None
			self.addressCode = None
			self.countryCode = None

		def getapiname(self):
			return 'jingdong.com.jd.address.international.glsc.GlscAddressCodingServiceWS.parseAddressCoding'

			




