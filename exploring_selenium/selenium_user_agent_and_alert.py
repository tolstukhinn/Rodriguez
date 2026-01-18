import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://demoqa.com/alerts")

ALERT_BUTTON = ("xpath", "//button[@id='alertButton']")
TIMER_ALERT_BUTTON = ("xpath", "//button[@id='timerAlertButton']")
CONFIRM_BUTTON = ("xpath", "//button[@id='confirmButton']")
PROMT_BUTTON = ("xpath", "//button[@id='promtButton']")

driver.find_element(*ALERT_BUTTON).click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)

driver.find_element(*TIMER_ALERT_BUTTON).click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
alert.accept()
time.sleep(3)

driver.find_element(*CONFIRM_BUTTON).click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
alert.dismiss()
time.sleep(3)

driver.find_element(*PROMT_BUTTON).click()
time.sleep(3)
alert = wait.until(EC.alert_is_present())
alert.send_keys("Nikita")
alert.accept()
time.sleep(3)










# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--remote-debugging-port=9222")
# driver = webdriver.Chrome(options=options)
# driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
# driver.get("https://vk.com")
# time.sleep(3)