from jd.api.base import RestApi

class ComJdJinVenderHandlerOpenStatementFacadeListStatementRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startTime = None
			self.status = None
			self.pageNo = None
			self.pageSize = None
			self.endTime = None
			self.statementId = None

		def getapiname(self):
			return 'jingdong.com.jd.jin.vender.handler.open.StatementFacade.listStatement'

			




