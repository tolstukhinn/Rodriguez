import time
from selenium import webdriver

# Опции
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
options.add_argument("--window-size=2560,1440")
# options.page_load_strategy = "normal"
# options.page_load_strategy = "eager"

FILE_UPLOAD_FIELD = ("xpath", "//input[@id='uploadFile']")

# Инициализация
driver = webdriver.Chrome(options=options)
driver.get("https://demoqa.com/upload-download")

file_field = driver.find_element(*FILE_UPLOAD_FIELD)
file_field.send_keys(r"C:\Users\User\PycharmProjects\Rodriguez\exploring_selenium\pictures\example.jpeg")


time.sleep(5)