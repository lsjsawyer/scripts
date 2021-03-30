from base.bases import Bases
from elements.hsl_elements import ElementsHSL



class OpenInHsl(Bases):

    def __init__(self, driver):
        Bases.__init__(self, driver)

    def open_rules_click_agrees(self):
        self.click_element(ElementsHSL.login_for_agree_rules_button_id)
        self.click_element(ElementsHSL.login_for_agree_system_power_id)
        self.click_element(ElementsHSL.login_for_agree_system_power_id)
        # self.click_element(ElementsHSL.open_first_page_level_power_xpath)
        self.click_element(ElementsHSL.go_to_mine_page_xpath)
        self.click_element(ElementsHSL.close_learn_some_id)
        self.click_element(ElementsHSL.open_login_to_hsl_id)
        self.click_element(ElementsHSL.input_id_for_login_button_id)
        self.send_element(ElementsHSL.input_id_for_login_button_id, "13120683383")
        self.click_element(ElementsHSL.input_password_for_login_button_id)
        self.send_element(ElementsHSL.input_password_for_login_button_id, "aini1314")
        self.click_element(ElementsHSL.login_button_id)


    def get_result(self):
        # res = self.get_element(ElementsHSL.get_first_assert_text_xpath).text
        res = self.get_element(ElementsHSL.get_username_id).text
        return res
