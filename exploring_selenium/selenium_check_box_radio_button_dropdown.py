import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


# driver.get("https://demoqa.com/checkbox")
# checkbox = driver.find_element("xpath", "//label[@for='tree-node-home']")
# toggle = driver.find_element("xpath", "//button[@class='rct-collapse rct-collapse-btn']")
# checkbox2 = driver.find_element("xpath", "//span[@class='rct-checkbox']")
# toggle.click()
# time.sleep(3)
# checkbox2.click()
# time.sleep(3)


# driver.get("https://demoqa.com/radio-button")
# YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']")
# YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']")
# IMPRESSIVE_RADIO_BUTTON = ("xpath", "//input[@id='impressiveRadio']")
# NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")
# print(driver.find_element(*NO_RADIO_BUTTON).is_enabled())
# if driver.find_element(*NO_RADIO_BUTTON).is_enabled():
#     driver.find_element(*NO_RADIO_BUTTON).click()
# driver.find_element(*YES_RADIO_BUTTON).click()
# print(driver.find_element(*YES_RADIO_BUTTON).is_selected())
# time.sleep(3)


# driver.get("https://the-internet.herokuapp.com/dropdown")
# DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
# dropdown = Select(driver.find_element(*DROPDOWN_ELEMENT))
# # dropdown.select_by_index(1)
# # dropdown.select_by_value("2")
# dropdown.select_by_visible_text("Option 2")
# time.sleep(2)


driver.get("https://demoqa.com/select-menu")
MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")
select = driver.find_element(*MULTISELECT)
select.send_keys("Green")
time.sleep(2)
assert select.get_attribute("value") == "Green", "Error in value Green"
select.send_keys(Keys.ENTER)
time.sleep(2)
select.send_keys(Keys.ESCAPE)
time.sleep(2)









