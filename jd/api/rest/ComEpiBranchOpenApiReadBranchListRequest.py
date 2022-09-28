from jd.api.base import RestApi

class ComEpiBranchOpenApiReadBranchListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.countryId = None
			self.provinceId = None
			self.cityId = None
			self.branchId = None
			self.branchStatus = None
			self.pageSize = None
			self.branchName = None
			self.pageIndex = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.epi.BranchOpenApiRead.branchList'

			




