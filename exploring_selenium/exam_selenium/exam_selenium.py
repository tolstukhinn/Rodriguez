# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = webdriver.ChromeOptions()
# options.add_argument("--window-size=2560,1440")
# options.add_argument("--incognito")
# options.add_experimental_option("prefs", {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False
#     }
# )
#
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.saucedemo.com")
#
# # Поиск локаторов
# username_field = driver.find_element("xpath", "//input[@id='user-name']")
# password_field = driver.find_element("xpath", "//input[@id='password']")
# login_button = driver.find_element("xpath", "//input[@id='login-button']")
#
# # Авторизация и проверка страницы по URL
# username_field.clear()
# username_field.send_keys("standard_user")
# password_field.clear()
# password_field.send_keys("secret_sauce")
# time.sleep(2)
# login_button.click()
# assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Invalid URL"
#
# # Сортировка товаров
# dropdown_element = driver.find_element("xpath", "//select[@class='product_sort_container']")
# sort_element = driver.find_element("xpath", "//option[@value='lohi']")
# dropdown_element.click()
# sort_element.click()
# time.sleep(2)
#
# # Добавление товаров в корзину
# add_backpack = driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
# add_t_shirt = driver.find_element("xpath", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
# add_backpack.click()
# add_t_shirt.click()
# time.sleep(2)
#
# # Переход в корзину и проверка страницы по URL
# cart_element = driver.find_element("xpath", "//a[@class='shopping_cart_link']")
# cart_element.click()
# assert driver.current_url == "https://www.saucedemo.com/cart.html", "Invalid URL"
# time.sleep(2)
#
# # Удаление товара из корзины и переход на чекаут
# remove_t_shirt = driver.find_element("xpath", "//button[@id='remove-test.allthethings()-t-shirt-(red)']")
# checkout_button = driver.find_element("xpath", "//button[@id='checkout']")
# remove_t_shirt.click()
# time.sleep(2)
# checkout_button.click()
#
# # Поиск локаторов
# first_name_field = driver.find_element("xpath", "//input[@id='first-name']")
# last_name_field = driver.find_element("xpath", "//input[@id='last-name']")
# zip_field = driver.find_element("xpath", "//input[@id='postal-code']")
# continue_button = driver.find_element("xpath", "//input[@id='continue']")
# time.sleep(2)
#
# # Заполнение полей ввода и переход на второй чекаут
# first_name_field.clear()
# first_name_field.send_keys("Nikita")
# last_name_field.clear()
# last_name_field.send_keys("Tolstukhin")
# zip_field.clear()
# zip_field.send_keys("12345")
# time.sleep(2)
# continue_button.click()
# time.sleep(2)
#
# # Проверка страницы по URL
# assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Invalid URL"
#
# # Оформление заказа и возврат на домашнюю страницу
# finish_button = driver.find_element("xpath", "//button[@id='finish']")
# finish_button.click()
# time.sleep(2)
# back_home_button = driver.find_element("xpath", "//button[@id='back-to-products']")
# back_home_button.click()
# assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Invalid URL"
# time.sleep(2)
#
# # Выход из системы
# burger_button = driver.find_element("xpath", "//button[@id='react-burger-menu-btn']")
# logout_button = driver.find_element("xpath", "//a[@id='logout_sidebar_link']")
# burger_button.click()
# time.sleep(2)
# logout_button.click()
# assert driver.current_url == "https://www.saucedemo.com/", "Invalid URL"
# time.sleep(2)
#
#
#
