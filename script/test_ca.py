# -*- coding: utf-8 -*-
# import sys
# sys.path.append("/root/monitoring")
import allure
import pytest
from base.get_driver import get_xiaomi_mix_8_no_session_driver
from base.getfiledata import GetFileData
from base.pages import LMPage
from selenium.common.exceptions import TimeoutException

def get_account():
    suc_list = []
    fail_list = []
    account_data = GetFileData().get_yaml_data("test_account")
    for i in account_data:
        if (account_data.get(i)).get("merchants_data"):
            fail_list.append((i, account_data.get(i).get("account"), account_data.get(i).get("passwd"),
                              account_data.get(i).get("merchants_data")))
        else:
            suc_list.append((i, account_data.get(i).get("account"), account_data.get(i).get("passwd"),
                             account_data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}



@allure.feature("ca认证测试")
class TestHuanShaouLv:

    def setup_class(self):
        self.driver = get_xiaomi_mix_8_no_session_driver("com.livermore.security", ".module.trade.view.StartActivity")
        self.page = LMPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @allure.story("ca弹窗测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("https://www.bugclose.com/testCase.html?id=3405&projectId=38335")
    @allure.step(title="预开户用户进入招商银行银证转账页面,弹出ca认证弹窗")
    @pytest.mark.parametrize("case_num, account, passwd, expect_data", get_account().get("suc"))
    def test_01(self, case_num, account, passwd, expect_data):
        self.page.market_page_lm().go_to_mine_page()
        self.page.mine_page_lm().log_in_correct_account(account, passwd)
        self.page.turn_to_money_page_lm().go_to_mainland_bank_card_page()
        try:
            ca_pop_result = self.page.turn_to_money_page_lm().get_ca_pop_result()
            try:
                assert expect_data in ca_pop_result
                self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
            except AssertionError:
                self.page.turn_to_money_page_lm().screen_shot("判定错误截图")
                self.page.turn_to_money_page_lm().from_merchants_bank_details_page_back_to_mine_page()
                assert False
        except TimeoutException:
            self.page.turn_to_money_page_lm().screen_shot("超时错误截图")
            self.page.turn_to_money_page_lm().from_merchants_bank_details_page_back_to_mine_page()
            assert False


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("ca弹窗测试")
    @allure.testcase("https://www.bugclose.com/testCase.html?id=3405&projectId=38335")
    @allure.step(title="预开户用户点击转入股票,弹出ca认证弹窗")
    def test_02(self):
        self.page.market_page_lm().go_to_mine_page()
        self.page.mine_page_lm().log_in_correct_account("105016423000", "lm123456")
        self.page.turn_to_money_page_lm().turn_into_stock()
        try:
            ca_pop_result = self.page.turn_to_money_page_lm().get_ca_pop_result()
            try:
                assert "请您进行客户身份信息安全认证" in ca_pop_result
                self.page.turn_to_money_page_lm().from_turn_into_money_page_back_to_mine_page()
            except AssertionError:
                self.page.turn_to_money_page_lm().screen_shot("判定错误截图")
                self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
                assert False
        except TimeoutException:
            self.page.turn_to_money_page_lm().screen_shot("超时错误截图")
            self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
            assert False


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("ca弹窗测试")
    @allure.testcase("https://www.bugclose.com/testCase.html?id=3405&projectId=38335")
    @allure.step(title="已开户用户点击银证转账银行,进入该银行详细信息页面")
    @pytest.mark.parametrize("case_num, account, passwd, merchants_data", get_account().get("fail"))
    def test_03(self, case_num, account, passwd, merchants_data):
        self.page.market_page_lm().go_to_mine_page()
        self.page.mine_page_lm().log_in_correct_account(account, passwd)
        self.page.turn_to_money_page_lm().go_to_mainland_bank_card_page()
        try:
            merchants_bank_page_result = self.page.turn_to_money_page_lm().get_merchants_bank_details()
            try:
                assert merchants_data in merchants_bank_page_result
                self.page.turn_to_money_page_lm().from_merchants_bank_details_page_back_to_mine_page()
            except AssertionError:
                self.page.turn_to_money_page_lm().screen_shot("判定错误截图")
                self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
                assert False
        except TimeoutException:
            self.page.turn_to_money_page_lm().screen_shot("超时错误截图")
            self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("ca弹窗测试")
    @allure.testcase("https://www.bugclose.com/testCase.html?id=3405&projectId=38335")
    @allure.step(title="已开户用户点击转入股票,进入转入股票详情页面")
    def test_04(self):
        self.page.market_page_lm().go_to_mine_page()
        self.page.mine_page_lm().log_in_correct_account("10501642300", "lm123456")
        self.page.turn_to_money_page_lm().turn_into_stock()
        try:
            transfer_stock_page_result = self.page.turn_to_money_page_lm().get_transfer_stock_page_result()
            try:
                assert "转出账户姓名需与利弗莫尔" in transfer_stock_page_result
                self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
            except AssertionError:
                self.page.turn_to_money_page_lm().screen_shot("判定错误截图")
                self.page.turn_to_money_page_lm().from_yinzheng_moneyin_back_to_mine_page()
                assert False
        except TimeoutException:
            self.page.turn_to_money_page_lm().screen_shot("超时错误截图")
            self.page.turn_to_money_page_lm().from_turn_into_money_page_back_to_mine_page()
            assert False
















