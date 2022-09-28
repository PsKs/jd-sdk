from jd.api.base import RestApi

class ComJdJinVenderHandlerOpenStatementFacadeOrderSettlementListRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.startHappenTime = None
			self.pageSize = None
			self.endHappenTime = None
			self.pageNo = None
			self.language = None
			self.orderId = None

		def getapiname(self):
			return 'jingdong.com.jd.jin.vender.handler.open.StatementFacade.orderSettlementList'

			




