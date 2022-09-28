from jd.api.base import RestApi

class ComJdwlApiOrderTrackSiteJsfExportOrderTrackSiteExportAddIntlOrderTrackRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.orderId = None
			self.systemType = None
			self.messageType = None
			self.msgTime = None
			self.locale = None
			self.content = None
			self.title = None
			self.operatorName = None
			self.systemName = None
			self.token = None
			self.locale1 = None
			self.clientBUId = None
			self.timezoneId = None

		def getapiname(self):
			return 'jingdong.com.jdwl.api.order.track.site.jsf.export.OrderTrackSiteExport.addIntlOrderTrack'

			




