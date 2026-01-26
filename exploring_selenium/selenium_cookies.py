import json
import os.path
import time
from selenium import webdriver
from cookies_manager import CookieManager

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/ru/login")
cookie_manager = CookieManager(driver)

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")



if os.path.exists("cookies.json"):
    cookie_manager.load_cookies()
else:
    driver.find_element(*LOGIN_FIELD).send_keys("testim_cookies@gmail.com")
    time.sleep(5)
    driver.find_element(*PASSWORD_FIELD).send_keys("Nikita110299!")
    time.sleep(5)
    driver.find_element(*SUBMIT_BUTTON).click()
    time.sleep(5)
    cookie_manager.save_cookies()

time.sleep(5)



# input()
#
# cookies = driver.get_cookies()
#
# with open('cookies.json', 'w') as file:
#     json.dump(cookies, file, indent=4)



# driver.delete_all_cookies()
#
# with open("cookies.json", "r") as file:
#     cookies = json.load(file)
#
# for cookie in cookies:
#     driver.add_cookie(cookie)
# time.sleep(3)
# driver.refresh()
# time.sleep(3)



