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

class test:
    def __init__(self, udid=None, appPackage=None, appActivity=None) -> None:
        self.platformName='Android'
        self.automationName='uiautomator2'
        self.deviceName='Android'
        self.appPackage= appPackage#'com.code2lead.kwad'
        self.appActivity=appActivity #'com.code2lead.kwad.MainActivity'
        self.udid=udid
        # language='en',
    def setUp(self):
        capabilities = dict(
        platformName=self.platformName,
        automationName=self.automationName,
        deviceName=self.deviceName,
        appPackage=self.appPackage,
        appActivity=self.appActivity,
        udid=self.udid
        # language='en',
        # locale='US'
        )
        url = 'http://localhost:4723/wd/hub'
        option=UiAutomator2Options().load_capabilities(capabilities)
        return webdriver.Remote(url, options=option)
    def wait(self, driver,xpath):
        return  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    def scroll_find2(self, driver,text):
        return  WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector()).scrollIntoView(text("{text}"))')))
    def scroll_find3(self, driver,xpath):
        return  WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector()).scrollIntoView(xpath("{xpath}"))')))
    def long_click(self, driver, element):
        action = ActionChains(driver)
        action.click_and_hold(element).perform()

    def scroll_find4(self, driver, xpath):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().xpath("{xpath}"))')))

    
    def wait2(self, driver, xpath):
        return WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException]).until(lambda x: x.find_element(AppiumBy.XPATH,xpath))
    def scroll_find(self, driver, text):
        return WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException]).until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector()).scrollIntoView(text("{text}"))'))


    def scroll(self,driver):
        wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
        
        ele = wait.until(lambda  x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("TAB ACTIVITY")'))
        ele.click()
        
        
        print("Device Width and Height : ",driver.get_window_size())
        #out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
        deviceSize = driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        
        ######Right to Left#######
        startx = screenWidth*8/9
        endx = screenWidth/9
        starty = screenHeight/2
        endy = screenHeight/2
        
        
        ###### Left to Right    #######
        startx2 = screenWidth/9
        endx2 = screenWidth*8/9
        starty2 = screenHeight/2
        endy2 = screenHeight/2
        
        actions = TouchAction(driver)
        actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
        sleep(2)
        actions.long_press(None,startx2,starty2).move_to(None,endx2,endy2).release().perform()
            



        # ele.click()
        # actions = TouchAction(driver)
        # #actions.tap(None,700,1990,1)
        # # if ele.is_displayed():
        # sleep(5)
        # actions.tap(element=ele, x=500, y=2018).perform()

        # self.long_click(driver=driver, element=element)

        # action = ActionChains(driver)
        # action.click_and_hold(ele).perform()
        # ele.click()
        sleep(5)

    def run(self):
        
        driver = self.setUp()
        # self.test_find_battery(driver=driver)
        self.scroll(driver=driver)

if __name__ == '__main__':
    test(udid='R58NC2W4ZQK', appPackage="com.code2lead.kwad", appActivity='com.code2lead.kwad.MainActivity').run()


#         ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
# ele_index.click()


# ele_classname = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
# ele_classname.send_keys("Skill2Lead")

# ele_xpath2 = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
# ele_xpath2.send_keys("Skill2lead.com")
 

# ele_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("ENTER SOME VALUE")') # Type-2
# ele_text.click()

# ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("Btn3")')
# ele_index.click()


# element = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")
 
# for x in element:
#     print(x.text)
 
# for x in element:
#     button = x.text
#     if button == "ScrollView":
#         x.click()
#         break

# wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
 
# ele = wait.until(lambda  x: x.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue"))
# ele.click()
 
# ele = wait.until(lambda  x: x.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText"))
# ele.send_keys("Skill2Lead")
# driver.press_keycode(67)
# driver.press_keycode(64)


# driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
# print("Is Displayed : ",element.is_displayed())
# print("Is Enabled : ",element.is_enabled())
# print("Is selected : ",element.is_selected())
# print("Size : ",element.size)
# print("Location : ",element.location)