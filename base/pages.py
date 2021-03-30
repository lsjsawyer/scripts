from page.hsl_open_page import OpenInHsl
from page.lm_mine_page import MinePage
from page.lm_mine_page import MarketPage
from page.turn_to_money_page import TurnToMoneyPage

class HslPage:
    def __init__(self, driver):
        self.driver = driver

    def open_hsl(self):
        return OpenInHsl(self.driver)

class LMPage:
    def __init__(self, driver):
        self.driver = driver

    def mine_page_lm(self):
        return MinePage(self.driver)

    def market_page_lm(self):
        return MarketPage(self.driver)

    def turn_to_money_page_lm(self):
        return TurnToMoneyPage(self.driver)
