import logging
import time
from datetime import datetime, timedelta

from bubot_helpers.ExtException import ExtException, ExtTimeoutError, NotAvailable
from bubot_helpers.Helper import get_tzinfo
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException, \
    SessionNotCreatedException, StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import DEFAULT_EXECUTABLE_PATH
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from .ScenarioExceptions import *
from .ScenarioState import *

tz_info = get_tzinfo()


class SeleniumScenario:
    _pages = []
    _timeout_after_click = 1
    file = __file__

    def __init__(self, *, proxy=None, props=None, driver=None, navigate_timeout=120, headless=False,
                 executable_path=None, log=None):
        self.log = log if log else logging.getLogger('SeleniumScenario')
        self.props = props
        self.loaded = None
        self.headless = headless
        self.executable_path = executable_path
        self.proxy = proxy
        self.temp = dict()
        self.driver = driver
        self.navigate_timeout = navigate_timeout
        self.navigate_deadline = None
        self.navigate_url = None

    @staticmethod
    def get_selenium_executable_path(executable_path=None, config_path=None):
        if executable_path == 'ChromeDriverManager':
            executable_path = ChromeDriverManager().install()
        return executable_path

    @classmethod
    def check_live(cls, driver, *, headless=False, proxy=None, executable_path=None):
        try:
            driver.execute(Command.DELETE_ALL_COOKIES)
            return driver
        except Exception as err:
            return cls.init_driver(headless=headless, proxy=proxy, executable_path=executable_path)

    @staticmethod
    def init_driver(*, headless=False, proxy=None, executable_path=None):

        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("start-maximized")
            # options.add_argument('--remote-debugging-port=9222')
            options.add_argument("--headless")
            options.add_argument("--incognito")
            # options.add_argument("--crash-dumps-dir=/tmp")
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-dev-shm-usage")  # https://github.com/puppeteer/puppeteer/issues/1834
            options.add_argument("--disable-browser-side-navigation")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
            # options.add_argument("--disable-cache")
            # options.add_argument("--disable-application-cache")
            # options.add_argument("--single-process")
            # options.add_argument("--aggressive-cache-discard")
            options.add_argument("--disk-cache-size=0")
            # options.add_argument("--dns-prefetch-disable")
            # options.add_argument("--no-proxy-server")
            # options.add_argument("--log-level=3")
            options.add_argument("--silent")
            options.add_argument("enable-automation")

            # options.add_argument("--disable-default-apps")
            # options.add_argument("--disable-offline-load-stale-cache")
            # options.add_argument("--remote-debugging-port=0")

        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
        executable_path = executable_path or DEFAULT_EXECUTABLE_PATH
        try:
            return Chrome(
                executable_path=executable_path,
                # service=Service(executable_path),
                options=options
            )
        except SessionNotCreatedException as err:
            raise ExtTimeoutError(parent=err, message='Selenium not created')
        except Exception as err:
            raise ExtException(parent=err,
                               dump={"executable_path": executable_path, "headless": headless}) from err

    def get_cookies(self):
        try:
            _raw_cookies = self.driver.get_cookies()
            # _cookies = {}
            # for elem in _raw_cookies:
            #     _cookies[elem['name']] = elem['value']
            _cookies = ""
            for elem in _raw_cookies:
                _cookies += f"{elem['name']}={elem['value']}; "
            return _cookies
        except Exception as err:
            raise ExtException(parent=err, action='get_cookies') from err

    @classmethod
    def is_loaded(cls, current_url):
        raise NotImplementedError()

    @staticmethod
    def print_current_time():
        return time.strftime('%H:%M', time.localtime())

    def navigate(self, url):
        self.driver.get(url)
        self.navigate_url = url
        while True:
            try:
                WebDriverWait(self.driver, self.navigate_timeout).until(lambda driver: self.check_page_loaded(driver))
            except TimeoutException:
                print(f'timeout {self.print_current_time()}')
                self.driver.quit()
                raise TimeoutError()
            try:
                return self.check_page()
            except NotLoaded:
                continue

    def set_deadline(self):
        if self.navigate_timeout:
            self.navigate_deadline = datetime.now() + timedelta(seconds=self.navigate_timeout)

    def check_navigate_timeout(self, detail):
        if self.navigate_deadline and datetime.now() > self.navigate_deadline:
            raise ExtTimeoutError(detail=detail, dump={'current_url': self.driver.current_url})

    def navigate_async(self, url):
        if isinstance(url, str):
            _url = url
        else:
            _url = url.page_url
        try:
            _url = _url[:-1] if _url[-1] == '*' else _url
            self.navigate_url = _url

            self.set_deadline()
            self.driver.get(_url)
            time.sleep(0.1)
        except Exception as err:
            if str(err).startswith('Message: unknown error: net::ERR_CONNECTION_REFUSED'):
                raise NotAvailable(detail=_url) from err
            raise NotAvailable(parent=err, detail=_url)

    def wait_navigate(self, destination=None, timeout=1):
        while not self.check_navigate(destination):
            time.sleep(timeout)

    def check_navigate(self, destination=None):
        try:
            current_url = self.driver.current_url
            self.check_navigate_timeout(
                f'navigate {self.navigate_url if destination is None else destination.__name__}')
            for page in self._pages:
                try:
                    _is_page = page.is_page(self.driver, current_url=current_url)
                except Exception as err:
                    raise ExtException(
                        parent=err,
                        message='Определение страницы содержит ошибку',
                        detail=f'{page.__name__} {err}'
                    )
                if _is_page:
                    try:
                        _is_loaded = page.is_loaded(self.driver, current_url=current_url, destination=destination)
                    except StaleElementReferenceException:
                        self.props['stale'] = page
                        _is_loaded = False
                    except NoSuchElementException:
                        _is_loaded = False
                    if _is_loaded:
                        if page.on_after_loaded(self, destination=destination):
                            return True if destination is None else page.is_page(self.driver, current_url=destination)
        except Capcha:
            self.state = CAPTCHA
        except Suspicious:
            self.state = SUSPICIOUS
        except WebDriverException as err:
            self.state = DISCONNECTED
            raise ExtException(parent=err) from err
        except Exception as err:
            raise ExtException(parent=err) from err
        return False

    def __del__(self):
        pass
        # self.quit()

    def quit(self):
        if self.driver:
            self.driver.quit()
            time.sleep(1)

    @classmethod
    def check_page_loaded(cls, driver):
        try:
            current_url = driver.current_url
            for page in cls._pages:
                if page.is_page(driver, current_url=current_url):
                    return page.is_loaded(driver, current_url=current_url)
        except NoSuchElementException:
            return False

    def check_page(self):
        current_url = self.driver.current_url
        for page in self._pages:
            if page.is_page(self.driver, current_url=current_url):
                try:
                    return page.on_after_loaded(self)
                except Exception as err:
                    raise ExtException(parent=err, message='Error on after loaded page', detail=page.__name__)
        pass

    def get_prop(self, name, default=None):
        return self.props.get(name, default)

    def set_prop(self, name, value):
        self.props[name] = value

    def _run(self):
        raise NotImplementedError()

    def run(self, props=None):
        begin = datetime.now(tz_info)
        if props:
            self.props = props
        try:
            self._run()

            end = datetime.now(tz_info)
            if 'last_check' not in self.props:
                self.props['last_check'] = {}
            self.props['last_check']['begin'] = begin
            self.props['last_check']['end'] = end
            self.props['last_check']['duration'] = str(end - begin)
        except Exception as err:
            ext_err = ExtException(parent=err, action=f'{self.__class__.__name__}.run')
            self.props['last_error'] = ext_err.title
            raise ext_err from err
