# -*-  coding:utf-8 -*-
from appium import webdriver
import time


# server启动参数

desired_caps = {}

# 设备参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'

# app参数
desired_caps['appPackage'] = 'cn.goapk.market'
desired_caps['appActivity'] = 'com.anzhi.market.ui.MainActivity'

# 解决输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

HumanIcon = driver.find_element_by_class_name("android.widget.ImageView")
HumanIcon.click()