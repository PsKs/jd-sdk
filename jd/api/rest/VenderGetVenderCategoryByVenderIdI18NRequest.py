from jd.api.base import RestApi

class VenderGetVenderCategoryByVenderIdI18NRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)

		def getapiname(self):
			return 'jingdong.vender.getVenderCategoryByVenderIdI18N'

			




