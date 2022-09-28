from jd.api.base import RestApi

class ComEpiBranchOpenApiWriteUpdateStatusRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.branchId = None
			self.status = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.epi.branchOpenApiWrite.updateStatus'

			




