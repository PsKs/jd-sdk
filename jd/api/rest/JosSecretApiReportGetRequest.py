from jd.api.base import RestApi

class JosSecretApiReportGetRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.customer_user_id = None
			self.access_token = None
			self.server_url = None
			self.businessId = None
			self.text = None
			self.attribute = None

		def getapiname(self):
			return 'jingdong.jos.secret.api.report.get'

			




