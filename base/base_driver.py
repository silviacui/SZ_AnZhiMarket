# -*-  coding:utf-8 -*-
from appium import webdriver


def init_driver():
    # server启动参数
    desired_caps = {}

    # 设备参数
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'

    # app参数
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    # 解决输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)