from jd.api.base import RestApi

class ComJdSellerTrackApiTrackSynFacadeRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.time = None
			self.trackingNumber = None
			self.status = None
			self.context = None
			self.expressCompany = None

		def getapiname(self):
			return 'jingdong.com.jd.seller.track.api.TrackSynFacade'

			




