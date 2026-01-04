import time
from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

first_name_field = driver.find_element("xpath", "//input[@id='firstName']")
first_name_field.clear()
first_name_field.send_keys("Nikita")
assert first_name_field.get_attribute("value") == "Nikita", "Error in value firstName field"

last_name_field = driver.find_element("xpath", "//input[@id='lastName']")
last_name_field.clear()
last_name_field.send_keys("Tolstukhin")
assert last_name_field.get_attribute("value") == "Tolstukhin", "Error in value lastName field"

user_email_field = driver.find_element("xpath", "//input[@id='userEmail']")
user_email_field.send_keys(Keys.CONTROL+"A")
user_email_field.send_keys(Keys.BACKSPACE)
user_email_field.send_keys("tolstukhinn@yandex.ru")
assert user_email_field.get_attribute("value") == "tolstukhinn@yandex.ru", "Error in value userEmail field"

user_number_field = driver.find_element("xpath", "//input[@id='userNumber']")
user_number_field.clear()
user_number_field.send_keys("9232753111")
assert user_number_field.get_attribute("value") == "9232753111", "Error in value userNumber field"

subjectsInput_field = driver.find_element("xpath", "//input[@id='subjectsInput']")
subjectsInput_field.clear()
subjectsInput_field.send_keys("Python")
assert subjectsInput_field.get_attribute("value") == "Python", "Error in value subjectsInput field"

time.sleep(3)