from appium import  webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
# import unittest
from appium import webdriver
from selenium.webdriver import ActionChains
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException

 
desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '11'
# desired_caps['deviceName'] = 'Pixel'
# desired_caps['app'] = ('/Users/sujithreddy/Documents/Code2Lead/Others/kwad.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
option=UiAutomator2Options().load_capabilities(desired_caps )
driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",options=option)
 
# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
 
 
# ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))
 
# actions = TouchAction(driver)
# #actions.tap(None,700,1990,1)
# actions.tap(ele,940,2400,1)
# actions.perform()
 
# time.sleep(2)
# driver.quit()


 
wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
 
ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
ele.click()
 
ele_kw = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/ingvw"))
 
ele_lay = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/layout2"))
 
actions = TouchAction(driver)
 
actions.long_press(ele_kw).move_to(ele_lay).release().perform()
 
 
time.sleep(4)
driver.quit()