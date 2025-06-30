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
    xpath = '(//android.view.ViewGroup[@resource-id="com.tonycube.app.movietime:id/layoutSquare"])[2]'
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element.click()

    xpath = '//android.widget.TextView[@text="城市／地區"]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element2.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtSquare" and @text="基隆"]'
    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element3.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtTitle"]'
    element4 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element4.click()

    xpath = '//android.widget.Button[@content-desc="加入常用"]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()

    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element6 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element6.click()
    element6.click()

    xpath = '//android.widget.LinearLayout[@content-desc="常用"]'
    element7 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element7.click()

    if "177" in driver.page_source:
        print("Pass.")
    else:
        print("Fail.")


    print("MTTC1 has been tested.")
    time.sleep(10)
    
    #MTTC2

    xpath = '//android.widget.TextView[@text="城市／地區"]'
    element8 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element8.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtSquare" and @text="台北\n東區"]'
    element9 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element9.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtTitle" and @text="總督影城"]'
    element10 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element10.click()

    try:
        xpath = '//android.widget.Button[@content-desc="加入常用"]'
        element11 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element11.click()
        print("Pass.")
    except:
        print("It has been added to the favorite.")

    print("MTTC2 has been tested.")
    time.sleep(10)

    #MTTC3

    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element12 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element12.click()
    element12.click()

    xpath = '//android.widget.LinearLayout[@content-desc="常用"]'
    element13 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element13.click()
    time.sleep(3)
    try:
        
        # 建立手指輸入
        # 使用 W3C PointerInput 進行拖移操作
        finger = PointerInput("touch", "finger")
        

        start_x, start_y = 1004, 670
        end_x, end_y = 1004, 470

        actions = ActionChains(driver)
        #actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        print("Pass.")
        time.sleep(3)
    except Exception as e:
        print("Fail. ", e)
        os.system("pause")

    print("MTTC3 has been tested.")
    time.sleep(10)

    #MTTC4
    xpath = '//android.widget.TextView[@text="城市／地區"]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element2.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtSquare" and @text="基隆"]'
    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element3.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtTitle"]'
    element4 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element4.click()

    xpath = '//android.widget.Button[@content-desc="移除常用"]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()

    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element6 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element6.click()
    element6.click()

    xpath = '//android.widget.LinearLayout[@content-desc="常用"]'
    element7 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element7.click()
    time.sleep(2)
    if not "177" in driver.page_source:
        print("Pass.")
    else:
        print("Fail.")


    print("MTTC4 has been tested.")
    time.sleep(10)

    #MTTC5

    xpath = '//android.widget.TextView[@text="城市／地區"]'
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element2.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtSquare" and @text="台北\n東區"]'
    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element3.click()

    xpath = '//android.widget.TextView[@resource-id="com.tonycube.app.movietime:id/txtTitle" and @text="總督影城"]'
    element4 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element4.click()

    xpath = '//android.widget.Button[@content-desc="移除常用"]'
    element5 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element5.click()

    xpath = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    element6 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element6.click()
    element6.click()

    xpath = '//android.widget.LinearLayout[@content-desc="常用"]'
    element7 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    element7.click()

    time.sleep(2)
    if "目前" in driver.page_source:
        print("Pass.")
    else:
        print("Fail.")
    
    print("MTTC5 has been tested.")

    os.system("pause")

except Exception as e:
    print(f"❌ 發生錯誤: {e}")

driver.quit()
