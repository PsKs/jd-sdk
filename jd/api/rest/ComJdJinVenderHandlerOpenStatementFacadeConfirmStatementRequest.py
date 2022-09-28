from jd.api.base import RestApi

class ComJdJinVenderHandlerOpenStatementFacadeConfirmStatementRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.settlementId = None
			self.language = None

		def getapiname(self):
			return 'jingdong.com.jd.jin.vender.handler.open.StatementFacade.confirmStatement'

			




