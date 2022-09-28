from jd.api.base import RestApi

class ComJdAddressInternationalGlscGlscAddressCodingServiceWSGetChildrenRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.addressCode = None

		def getapiname(self):
			return 'jingdong.com.jd.address.international.glsc.GlscAddressCodingServiceWS.getChildren'

			




