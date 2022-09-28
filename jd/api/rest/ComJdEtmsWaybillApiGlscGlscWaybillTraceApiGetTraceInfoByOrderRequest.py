from jd.api.base import RestApi

class ComJdEtmsWaybillApiGlscGlscWaybillTraceApiGetTraceInfoByOrderRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.countryFlag = None
			self.orderCode = None
			self.locale = None

		def getapiname(self):
			return 'jingdong.com.jd.etms.waybill.api.glsc.GlscWaybillTraceApi.getTraceInfoByOrder'

			




