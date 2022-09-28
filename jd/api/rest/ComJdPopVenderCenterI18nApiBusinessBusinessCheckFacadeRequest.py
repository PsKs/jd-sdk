from jd.api.base import RestApi

class ComJdPopVenderCenterI18nApiBusinessBusinessCheckFacadeRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.businessTypes = None
			self.businessUnit = None

		def getapiname(self):
			return 'jingdong.com.jd.pop.vender.center.i18n.api.business.BusinessCheckFacade'

			




