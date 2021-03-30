from base.bases import Bases
from elements.livemore_elements import MinePageElements
from elements.livemore_elements import LoginPageElements
from elements.livemore_elements import SettingsPageElements
from elements.livemore_elements import HomePageElements

class MinePage(Bases):

    def __init__(self, driver):
        Bases.__init__(self, driver)

    def login(self, phone_num, pwd):
        self.click_element(MinePageElements.mine_page_button)
        self.click_element(MinePageElements.login_button_mine_page)
        self.send_element(LoginPageElements.phone_num_input_field, phone_num)
        self.send_element(LoginPageElements.phone_pwd_input_field, pwd)
        self.click_element(LoginPageElements.login_button_login_page)


    def log_in_correct_account(self, phone_num, pwd):
        all_class_name_xpath = self.get_elements(MinePageElements.class_name_xpath)
        class_name_text_list = []
        for i in all_class_name_xpath:
            class_name_text_list.append(i.text)
        if "登录"and "开户" in class_name_text_list:
            self.click_element(MinePageElements.login_button_mine_page)
            self.send_element(LoginPageElements.phone_num_input_field, phone_num)
            self.send_element(LoginPageElements.phone_pwd_input_field, pwd)
            self.click_element(LoginPageElements.login_button_login_page)
            self.click_element(MinePageElements.immediate_fund_transfer_button)
        else:
            self.click_element(MinePageElements.setting_button_mine_page)
            self.click_element(SettingsPageElements.logout_button)
            self.click_element(MinePageElements.login_button_mine_page)
            self.send_element(LoginPageElements.phone_num_input_field, phone_num)
            self.send_element(LoginPageElements.phone_pwd_input_field, pwd)
            self.click_element(LoginPageElements.login_button_login_page)
            self.click_element(MinePageElements.immediate_fund_transfer_button)

class MarketPage(Bases):

    def __init__(self, driver):
        Bases.__init__(self, driver)

    def go_to_mine_page(self):
        self.click_element(HomePageElements.mine_page_button)



