# import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class test:
    def __init__(self) -> None:
        pass
    def setUp(self):
        capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        # appPackage='com.code2lead.kwad',
        # appActivity='com.code2lead.kwad.MainActivity'
        # language='en',
        # locale='US'
        )
        url = 'http://localhost:4723/wd/hub'
        option=UiAutomator2Options().load_capabilities(capabilities)
        return webdriver.Remote(url, options=option)
    def wait(self, driver,xpath):
        return  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))

    def test_find_battery(self,driver):
        # element= self.wait(driver, '//android.widget.TextView[@resource-id="android:id/title" and @text="Connections"]')
        # element.click()
        # element = self.wait(driver, '//android.widget.Switch[@content-desc="Wi-Fi"]')
        # element.click()
        # sleep(5)
        # element = self.wait(driver, '//android.widget.Button[@content-desc="Btn1"]')
        # element.click()
        # sleep(2)
        for i in range(3):
            driver.press_keycode(22)
            sleep(2)
        # element = self.wait(driver, '//android.view.ViewGroup[@resource-id="com.samsung.android.app.notes:id/zoom_lock_tip"]')
        # element.send_keys("hello")



        
    
    def run(self):
        driver = self.setUp()
        self.test_find_battery(driver=driver)

if __name__ == '__main__':
    test().run()


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