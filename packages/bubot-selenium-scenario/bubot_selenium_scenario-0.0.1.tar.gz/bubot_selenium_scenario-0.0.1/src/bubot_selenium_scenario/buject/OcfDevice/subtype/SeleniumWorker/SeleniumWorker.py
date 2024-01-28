from bubot.buject.OcfDevice.subtype.Device.RedisQueueMixin import RedisQueueMixin
from bubot.buject.OcfDevice.subtype.VirtualServer.VirtualServer import VirtualServer
from bubot_selenium_scenario.buject.SeleniumScenario.SeleniumScenario import SeleniumScenario
from datetime import datetime
from bubot_selenium_scenario import __version__ as device_version


# _logger = logging.getLogger(__name__)


class SeleniumWorker(RedisQueueMixin, VirtualServer):
    version = device_version
    template = True
    file = __file__

    def __init__(self, **kwargs):
        self.storage = None
        self.redis = None
        self.queues = []
        self.selenium = None
        # self.selenium_headless = None
        # self.selenium_webdriver_path = None
        VirtualServer.__init__(self, **kwargs)
        RedisQueueMixin.__init__(self, **kwargs)
        self.selenium_executable_path = None
        self.selenium_headless = None
        self.selenium_last_init = None
        self.last_run_first_grade_auth = None
        self.last_run_ari_sef_pt = None
        self.driver = None

    async def on_pending(self):
        # self.init_driver()
        await RedisQueueMixin.on_pending(self)
        self.log.info('complete')
        self.set_param('/oic/mnt', 'currentMachineState', 'idle', save_config=True)
        pass

    def init_driver(self):
        selenium = self.get_param('/oic/con', 'selenium', {})
        self.selenium_headless = selenium.get('headless')
        self.selenium_executable_path = SeleniumScenario.get_selenium_executable_path(
            selenium.get('webdriver_path'))
        self.driver = SeleniumScenario.init_driver(headless=self.selenium_headless,
                                                   executable_path=self.selenium_executable_path,
                                                   proxy=selenium.get('proxy')
                                                   )
        self.selenium_last_init = datetime.now()

    async def close_driver(self):
        self.driver = None
        pass

    def check_selenium_live(self):
        if not self.driver:
            self.init_driver()
        self.driver = SeleniumScenario.check_live(self.driver, headless=self.selenium_headless,
                                                  executable_path=self.selenium_executable_path)

    async def on_cancelled(self):
        await RedisQueueMixin.on_cancelled(self)
        await VirtualServer.on_cancelled(self)
