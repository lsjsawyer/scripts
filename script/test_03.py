from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By



def test_sth():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8'
    desired_caps['deviceName'] = 'xiaomi_mix2_8.0'
    desired_caps['appPackage'] = "com.livermore.security"
    desired_caps['appActivity'] = ".module.trade.view.StartActivity"
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['noReset'] = True
    desired_caps['udid'] = '66c72b9'
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    sleep(3)
    # screen_size = driver.get_window_size()
    # height = screen_size.get('height')
    # width = screen_size.get('width')
    # driver.tap([(799/1080 * width, 1344/2030 * height)])
    # sleep(10)
    driver.find_element_by_xpath("//*[contains(@text, '我的')]").click()
    sleep(3)
    driver.find_element_by_xpath("//*[contains(@text, '立即转入资金')]").click()
    driver.keyevent(4)
    # sleep(3)
    # driver.tap([(799, 1344)])
    sleep(5)
    driver.quit()





if __name__ == '__main__':
    test_sth()