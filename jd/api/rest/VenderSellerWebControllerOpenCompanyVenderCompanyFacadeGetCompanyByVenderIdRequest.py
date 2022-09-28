from jd.api.base import RestApi

class VenderSellerWebControllerOpenCompanyVenderCompanyFacadeGetCompanyByVenderIdRequest(RestApi):
		def __init__(self,domain,port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.language = None

		def getapiname(self):
			return 'jingdong.vender.seller.web.controller.open.company.VenderCompanyFacade.getCompanyByVenderId'

			




