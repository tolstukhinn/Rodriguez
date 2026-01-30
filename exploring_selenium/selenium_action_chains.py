import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10, 1)
action = ActionChains(driver)

# action.click().perform()
# driver.get("https://demoqa.com/buttons")
#
# DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
# RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
# LEFT_CLICK_BUTTON = ("xpath", "//button[text()='Click Me']")
#
# BUTTON1 = driver.find_element(*DOUBLE_CLICK_BUTTON)
# action.double_click(BUTTON1).perform()
# time.sleep(3)
#
# BUTTON2 = driver.find_element(*RIGHT_CLICK_BUTTON)
# action.context_click(BUTTON2).perform()
# time.sleep(3)
#
# BUTTON3 = driver.find_element(*LEFT_CLICK_BUTTON)
# action.click(BUTTON3).perform()
# time.sleep(3)

# driver.get("https://demoqa.com/menu")
#
# STEP_1_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
# STEP_2_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST »']")
# STEP_3_LOCATOR = ("xpath", "//a[text()='Sub Sub Item 2']")
#
# STEP_1 = driver.find_element(*STEP_1_LOCATOR)
# STEP_2 = driver.find_element(*STEP_2_LOCATOR)
# STEP_3 = driver.find_element(*STEP_3_LOCATOR)
#
# action.move_to_element(STEP_1).pause(3).move_to_element(STEP_2).pause(3).move_to_element(STEP_3).click().perform()
# time.sleep(3)

driver.get("https://demoqa.com/droppable")

SOURCE_LOCATOR = ("xpath", "//div[@id='draggable']")
TARGET_LOCATOR = ("xpath", "//div[@id='droppable']")

SOURCE = driver.find_element(*SOURCE_LOCATOR)
TARGET = driver.find_element(*TARGET_LOCATOR)

action.drag_and_drop(SOURCE, TARGET).perform()
time.sleep(3)