from time import sleep

from base.bases import Bases
from elements.livemore_elements import TurnToMoneyPageElements
from elements.livemore_elements import MerchantsBanksBankTransferDetailsPage
from elements.livemore_elements import TransferToStockPage

class TurnToMoneyPage(Bases):

    def __init__(self, driver):
        Bases.__init__(self, driver)

    def go_to_mainland_bank_card_page(self):
        # self.click_element(TurnToMoneyPageElements.bank_card_main_land)
        # self.click_element(TurnToMoneyPageElements.into_the_stock)
        self.click_element(TurnToMoneyPageElements.hangkang_area_bank_securities_tansfer)
        self.click_element(TurnToMoneyPageElements.zhaoshang_bank)

    def get_ca_pop_result(self):
        get_result_ca = self.get_element(TurnToMoneyPageElements.ca_pop_up_window, timeout=10)
        return get_result_ca.text

    def turn_into_stock(self):
        self.get_element(TurnToMoneyPageElements.hangkang_area_bank_securities_tansfer)
        self.coordinates_click(799/1080, 1344/2030)

    def from_yinzheng_moneyin_back_to_mine_page(self):
        self.click_element(TurnToMoneyPageElements.back_button_hangkang_yin_zheng)
        self.get_element(TurnToMoneyPageElements.hangkang_area_bank_securities_tansfer)
        # self.click_element(TurnToMoneyPageElements.back_button_hangkang_yin_zheng)
        self.driver.keyevent(4)

    def from_turn_into_money_page_back_to_mine_page(self):
        self.get_element(TurnToMoneyPageElements.hangkang_area_bank_securities_tansfer)
        self.driver.keyevent(4)

    def get_merchants_bank_details(self):
        get_result_for_merchants_page = self.get_element(MerchantsBanksBankTransferDetailsPage.how_to_open_merchants_banks_transfor, timeout=10)
        return get_result_for_merchants_page.text

    def from_merchants_bank_details_page_back_to_mine_page(self):
        self.click_element(TurnToMoneyPageElements.back_button_hangkang_yin_zheng)
        self.get_element(TurnToMoneyPageElements.zhaoshang_bank)
        self.click_element(TurnToMoneyPageElements.back_button_hangkang_yin_zheng)
        self.get_element(TurnToMoneyPageElements.hangkang_area_bank_securities_tansfer)
        self.driver.keyevent(4)

    def get_transfer_stock_page_result(self):
        get_result_for_transfer_stock_page = self.get_element(TransferToStockPage.transfer_stock_details, timeout=10)
        return get_result_for_transfer_stock_page.text
