from jd.api.base import RestApi

class CommonImageUploadFileRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.fileContent = None

		def getapiname(self):
			return 'jingdong.common.image.UploadFile'

			




