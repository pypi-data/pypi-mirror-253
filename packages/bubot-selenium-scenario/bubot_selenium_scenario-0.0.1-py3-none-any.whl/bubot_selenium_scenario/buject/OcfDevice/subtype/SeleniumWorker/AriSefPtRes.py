from bubot_helpers.ExtException import ExtException
from bubot.OcfResource.OcfResource import OcfResource
from bubot_BubotObj.SeleniumScenario.AriSefPt.Scenario import Scenario


class AriSefPtRes(OcfResource):

    async def render_POST_advanced(self, request, response):
        self.device.check_selenium_live()
        data = request.cn
        scenario = Scenario(driver=self.device.driver)
        scenario.run(data)
        response = request.generate_answer(data)
        self.device.close_driver()
        return self, response
