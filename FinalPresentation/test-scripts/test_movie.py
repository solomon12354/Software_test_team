import os
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.actions.interaction import POINTER
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction

from selenium.webdriver.support import expected_conditions as EC

os.environ["ANDROID_HOME"] = r"C:\Users\User\AppData\Local\Android\Sdk"
os.environ["ANDROID_SDK_ROOT"] = r"C:\Users\User\AppData\Local\Android\Sdk"

from appium import webdriver
from appium.options.android import UiAutomator2Options


options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "uiautomator2"
options.app = r"C:\Users\User\Downloads\movie.apk"
options.avd = "Pixel_7"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
# 你的測試程式碼...
# 等待元素並點擊
try:
    #MTTC1
    xpath = '(//android.widget.ImageView[@content-desc="選單圖示"])[1]'
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()

    xpath = '(//android.view.View[@resource-id="com.tonycube.app.movietime:id/viewBackground"])[1]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element2.click()

    xpath = '//android.widget.Button[@content-desc="加入收藏"]'
    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element3.click()

    

    xpath = '//android.widget.Button[@resource-id="android:id/button2"]'
    element4 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element4.click()

    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()
    element5.click()

    xpath = '(//android.widget.ImageView[@content-desc="選單圖示"])[5]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()



    try:
        xpath = '//android.widget.ImageView[@content-desc="電影海報"]'
        element6 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element6.click()
        print("Pass")
    except Exception as e:
        print("Fail")

    print("MVTC1 has been tested.")
    

    
    time.sleep(3)
    
     #MVTC2
    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()
    element5.click()

    xpath = '(//android.widget.ImageView[@content-desc="選單圖示"])[1]'
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()

    xpath = '//android.widget.LinearLayout[@content-desc="即將"]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element2.click() #
    '''
    xpath = '(//android.view.View[@resource-id="com.tonycube.app.movietime:id/viewBackground"])[1]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element3.click()
    '''

    try:
        xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtChName" and @text="私家偵探"]'
        element3 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element3.click()
        print("Pass")
    except Exception as e:
        print("Fail")

    print("MVTC2 has been tested.")
    

    #os.system("pause")

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

driver.quit()

