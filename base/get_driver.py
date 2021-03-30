from appium import webdriver


def get_xiaomi_mix_8_driver(pac, act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8'
    desired_caps['deviceName'] = 'xiaomi_mix2_8.0'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['udid'] = '66c72b9'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

def get_xiaomi_mix_8_no_session_driver(pac, act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8'
    desired_caps['deviceName'] = 'xiaomi_mix2_8.0'
    desired_caps['appPackage'] = pac
    desired_caps['appActivity'] = act
    desired_caps['resetKeyboard'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['noReset'] = True
    desired_caps['udid'] = '66c72b9'
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


