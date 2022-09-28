from jd.api.base import RestApi

class ComEpiBranchOpenApiReadBranchDetailRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.branchId = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.epi.branchOpenApiRead.branchDetail'

			




