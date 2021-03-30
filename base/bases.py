import os
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure
from datetime import datetime


class Bases:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, loc, timeout=30, once=1.0):
        return WebDriverWait(self.driver, timeout, once).until(lambda x: x.find_element(*loc))

    def get_elements(self, loc, timeout=30, once=1.0):
        return WebDriverWait(self.driver, timeout, once).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=30, once=1.0):
        self.get_element(loc, timeout, once).click()

    def send_element(self, loc, text, timeout=30, once=1.0):
        input_text = self.get_element(loc, timeout, once)
        input_text.clear()
        input_text.send_keys(text)

    def long_press(self, loc, wait_time, timeout=30, once=1.0):
        TouchAction(self.driver).press(self.get_element(loc, timeout, once)).wait(wait_time).release().perform()

    def swip_window_top_to_bottom(self):
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        self.driver.swipe(width * 0.5, height * 0.7, width * 0.5, height * 0.3, duration=3000)

    def swip_window_right_to_left(self):
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        self.driver.swipe(width * 0.9, height * 0.5, width * 0.2, height * 0.5, duration=3000)

    def swip_window_left_to_right(self):
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        self.driver.swipe(width * 0.2, height * 0.5, width * 0.9, height * 0.5, duration=3000)

    def scroll_screen(self, sc=1):
        sleep(2)
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        isinstance(sc, int)
        if sc == 1:
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, duration=3000)
        if sc == 2:
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, duration=3000)
        if sc == 3:
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, duration=3000)
        if sc == 4:
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, duration=3000)

    def screen_page(self):

        png_name ="./images/{}.png".format(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        self.driver.get_screenshot_as_file(png_name)
        with open(png_name, "rb") as f:
            allure.attach(f.read(), png_name, allure.attachment_type.PNG)

    def screen_shot(self, name):
        png_time = "./images/%s.png" % datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.driver.get_screenshot_as_file(png_time)
        allure.attach.file(r"%s" % png_time, attachment_type=allure.attachment_type.PNG,
                           name=name)


    def get_toast(self, toast):
        toast_xpath = (By.XPATH, "//*[contains(@text, '{}')]".format(toast))
        data = self.get_element(toast_xpath, timeout=5, once=0.5).text
        return data


    def sccren_in(self):
        TouchAction(self.driver).press(x=830, y=518).release().perform()

    def coordinates_click(self, wi, he):
        screen_size = self.driver.get_window_size()
        height = screen_size.get('height')
        width = screen_size.get('width')
        self.driver.tap([(wi * width, he * height)])

    def handle_windows(self):
        """处理弹窗"""
        try:
            # // 返回当前页面所有标签为classname的元素列表
            elements = self.driver.find_elements_by_class_name('android.widget.Button')
            while True:
                for element in elements:
                    if element.text == '允许':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
                    elif element.text == '始终允许':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
                    elif element.text == '确定':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
                    elif element.text == '取消':
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("取消")').click()
        except:
            print('未检测到弹窗')





