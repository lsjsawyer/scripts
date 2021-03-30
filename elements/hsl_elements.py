from selenium.webdriver.common.by import By



class ElementsHSL:

    login_for_agree_rules_button_id = (By.ID, "com.hsl.stock:id/txt_buy")
    login_for_agree_system_power_id = (By.ID, "android:id/button1")
    open_first_page_level_power_xpath = (By.XPATH, "//*[contains(@text, '涨停强度')]")
    get_first_assert_text_xpath = (By.XPATH, "//*[contains(@text, '涨停成功率')]")
    go_to_mine_page_xpath = (By.XPATH, "//*[contains(@bounds, '[864,1886][1080,2030]')]")
    close_learn_some_id = (By.ID, "com.hsl.stock:id/tv_cancel")
    open_login_to_hsl_id = (By.ID, "com.hsl.stock:id/linearPayDetail")
    input_id_for_login_button_id = (By.ID, "com.hsl.stock:id/edit_phone_num")
    input_password_for_login_button_id = (By.ID, "com.hsl.stock:id/eidt_password")
    login_button_id = (By.ID, "com.hsl.stock:id/btn_login")
    get_username_id = (By.ID, "com.hsl.stock:id/tv_user_name")

