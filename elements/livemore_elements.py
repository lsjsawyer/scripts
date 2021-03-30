from selenium.webdriver.common.by import By

class HomePageElements:
    mine_page_button = (By.XPATH, "//*[contains(@text, '我的')]")



class LoginPageElements:
    phone_num_input_field = (By.ID, "com.livermore.security:id/et_phone")
    phone_pwd_input_field = (By.ID, "com.livermore.security:id/et_password")
    login_button_login_page = (By.ID, "com.livermore.security:id/tv_login")
    back_button_login_page = (By.ID, "com.livermore.security:id/imageBack")

class MinePageElements:
    mine_page_button = (By.XPATH, "//*[contains(@text, '我的')]")
    login_button_mine_page = (By.ID, "com.livermore.security:id/tv_login")
    setting_button_mine_page = (By.ID, "com.livermore.security:id/iv_setting")
    class_name_xpath = (By.XPATH, "//*[contains(@class, 'android.widget.TextView')]")
    immediate_fund_transfer_button = (By.ID, "com.livermore.security:id/layout_account")

class SettingsPageElements:
    logout_button = (By.ID, "com.livermore.security:id/tv_logout")

class TurnToMoneyPageElements:
    bank_card_main_land = (By.XPATH, "//*[contains(@text, '大陆地区银行卡')]")
    hangkang_area_bank_securities_tansfer = (By.XPATH, "//*[contains(@text, '香港地区银行卡（银证转账）')]")
    zhaoshang_bank = (By.XPATH, "//*[contains(@text, '招商银行香港分行')]")
    ca_pop_up_window = (By.XPATH, "//*[contains(@text, '非常感谢您选择利弗莫尔证券')]")
    back_button_hangkang_yin_zheng = (By.ID, "com.livermore.security:id/imageBack")


class MerchantsBanksBankTransferDetailsPage:
    how_to_open_merchants_banks_transfor = (By.XPATH, "//*[contains(@text, '存入资金前，需先在香港招商网银申请开通银证转账服务。')]")


class TransferToStockPage:
    transfer_stock_details = (By.XPATH, "//*[contains(@text, '*转出账户姓名需与利弗莫尔证券账户同名')]")

class BankSecuritiesTransferPageElements:
    pass

class TransferToTheStockPageElements:
    pass

class MainlandBankCardPageElements:
    pass

class HongKongBankCardPageElements:
    pass

class SecuritiesTradingPageElements:
    pass

class CAPageElements:
    pass


