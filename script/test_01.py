import os
import time

import allure
import pytest

from base.get_driver import get_xiaomi_mix_8_driver
from base.pages import HslPage
import allure
from base.bases import Bases

# blocker：阻塞缺陷(功能未实现，无法下一步)
# critical：严重缺陷(功能点缺失)
# normal： 一般缺陷(边界情况，格式错误)
# minor：次要缺陷(界面错误与ui需求不符)
# trivial： 轻微缺陷(必须项无提示，或者提示不规范)


class TestHslOpen:

    def setup_class(self):
        self.driver = get_xiaomi_mix_8_driver("com.hsl.stock", ".module.main.StartV2Activity")
        self.page = HslPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="打开app,进入我的页面,输入手机号密码,点击登陆")
    def test_01(self):
        self.page.open_hsl().open_rules_click_agrees()
        ass = self.page.open_hsl().get_result()
        allure.attach("13120683383", "手机号")
        allure.attach("aini1314", "密码")
        assert ass == "兔子人"
        # png_name = "./images" + os.sep + "{}.png".format(int(time.time()))
        png_time = "./images/%s.png" % int(time.time())
        self.driver.get_screenshot_as_file(png_time)
        allure.attach.file(r"%s" % png_time, attachment_type=allure.attachment_type.PNG,
                           name="Cileen")
        # ass = self.page.open_hsl().get_result()
        # assert ass == "涨停成功率"



    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step(title="这是test02的测试步骤")
    def test_02(self):
        allure.attach.file(r"./images/adc.png", attachment_type=allure.attachment_type.PNG,
                           name="Aileen")
        assert True

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step(title="这是test03的测试步骤")
    def test_03(self):
        print("---->test02<----")
        assert False

    @allure.severity(allure.severity_level.MINOR)
    @allure.step(title="这是test04的测试步骤")
    def test_04(self):
        print("---->test03<----")
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step(title="这是test05的测试步骤")
    def test_05(self):
        print("---->test04<----")
        assert True
