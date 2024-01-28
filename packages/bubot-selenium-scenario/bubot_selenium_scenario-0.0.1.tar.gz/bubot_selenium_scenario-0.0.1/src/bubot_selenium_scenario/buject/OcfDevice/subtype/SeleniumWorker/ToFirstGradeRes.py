import asyncio
from datetime import datetime, timedelta

from bubot_helpers.ExtException import ExtException, Unauthorized
from Bubot.OcfResource.OcfResource import OcfResource

from BubotObj.OcfDevice.subtype.ToFirstGrade.SchoolApi.SchoolApi import SchoolApi
from BubotObj.Draft.Draft import Draft
from BubotObj.Order.subtype.ToFirstGrade.ToFirstGrade import ToFirstGrade as Order
from BubotObj.SeleniumScenario.ToFirstGrade.Scenario import Scenario


class ToFirstGradeRes(OcfResource):

    async def render_POST_advanced(self, request, response):
        self.device.check_selenium_live()
        try:
            order = Order(None)
            order.init_by_data(request.cn['order'])
            self.device.log.info(f'process {order.data["login"]}')
            request.cn['need_update'] = False
            if order.data.get('check_access') != 'success':
                self.device.log.info(f'check_access begin {order.data["login"]}')
                await self.check_access(order)
                self.device.log.info(
                    f'check_access complete {order.data["login"]} - {order.data.get("check_access")}')
                request.cn['need_update'] = True
            if order.data.get('check_access') == 'success' and request.cn.get('check_order'):
                self.device.log.info(f'check_order begin {order.data["login"]}')
                await self.check_order(order)
                self.device.log.info(
                    f'check_order complete {order.data["login"]} - {order.data.get("check_order")}')
                request.cn['need_update'] = True
            request.cn["order"] = order.data
            response = request.generate_answer(request.cn)
            self.device.close_driver()
            return self, response
        except Exception as err:
            err1 = ExtException(parent=err)
            self.device.log.error(err1.title)
            raise err1 from err

    async def check_access(self, order):
        self.device.check_selenium_live()
        delay = self.device.get_param('/oic/con', 'gosuslugi_auth_delay', 55)
        if self.device.last_run_first_grade_auth:
            wait = (timedelta(seconds=delay) - (datetime.now() - self.device.last_run_first_grade_auth)).total_seconds()
            self.device.log.info(f'wait gosuslugi auth {wait}')
            if wait > 0:
                await asyncio.sleep(wait)
        scenario = Scenario(driver=self.device.driver, log=self.device.log)
        try:
            scenario.run(order.data)
            order.data['check_access'] = 'success'
            await asyncio.sleep(0)
        except Exception as err:
            err1 = ExtException(parent=err)
            order.data['last_error'] = err1.to_dict()
            order.data['check_access'] = err1.title
        finally:
            self.device.last_run_first_grade_auth = datetime.now()

    async def check_order(self, order):
        try:
            return await order.check()
        except Unauthorized:
            try:
                await self.check_access(order)
                if order.data.get('check_access') != 'success':
                    order.data['check_order'] = ""
                    return
                return await order.check()
            except Exception as err:
                err1 = ExtException(parent=err)
                order.data['last_error'] = err1.to_dict()
                order.data['check_order'] = err1.title
        except Exception as err:
            err1 = ExtException(parent=err)
            order.data['last_error'] = err1.to_dict()
            order.data['check_order'] = err1.title
