import time
import pytest
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.epic("FullFlow")
@pytest.mark.usefixtures("driver")

class TestFullFlow:

    @pytest.mark.full_flow
    @allure.title("Full E-commerce Flow Test")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://confluence.com", name="Documentation")

    def test_full_ecommerce_flow(self):
        self.authorize()
        self.sorting()
        self.add_backpack()
        self.go_to_cart()
        self.remove_item()
        self.filling_in_checkout_fields()
        self.go_to_second_checkout()
        self.placing_an_order()
        self.return_to_home_page()
        self.logout()

    def authorize(self):

        with allure.step("01. Открытие страницы авторизации."):
            self.driver.get("https://www.saucedemo.com/")
            assert self.driver.current_url == "https://www.saucedemo.com/", "Ошибка открытия login page"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Открытие login page",
                attachment_type=allure.attachment_type.PNG,
            )
        username_field = self.driver.find_element("xpath", "//input[@id='user-name']")
        password_field = self.driver.find_element("xpath", "//input[@id='password']")
        login_button = self.driver.find_element("xpath", "//input[@id='login-button']")
        username_field.clear()
        username_field.send_keys("standard_user")
        password_field.send_keys("")
        password_field.clear()
        password_field.send_keys("secret_sauce")

        with allure.step("02. Проверка заполнения полей авторизации."):
            username_field_actual_value = username_field.get_attribute("value")
            assert username_field_actual_value == "standard_user", "Ошибка в поле username"
            password_field_actual_value = password_field.get_attribute("value")
            assert password_field_actual_value == "secret_sauce", "Ошибка в поле password"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Поля авторизации заполнены корректно",
                attachment_type=allure.attachment_type.PNG,
            )
            login_button.click()
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Invalid URL"

        with allure.step("03. Успешная авторизация."):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Авторизация",
                attachment_type=allure.attachment_type.PNG,
            )

    def sorting(self):

        with allure.step("04. Сортировка товаров."):
            dropdown_element = self.driver.find_element("xpath", "//select[@class='product_sort_container']")
            sort_element = self.driver.find_element("xpath", "//option[@value='lohi']")
            dropdown_element.click()
            sort_element.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Сортировка товаров",
                attachment_type=allure.attachment_type.PNG,
            )

    def add_backpack(self):

        with allure.step("05. Товары добавлены в корзину."):
            add_backpack = self.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
            add_t_shirt = self.driver.find_element("xpath", "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
            add_backpack.click()
            add_t_shirt.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товары добавлены в корзину",
                attachment_type=allure.attachment_type.PNG,
            )

    def go_to_cart(self):

        with allure.step("06. Переход в корзину."):
            cart_element = self.driver.find_element("xpath", "//a[@class='shopping_cart_link']")
            cart_element.click()
            assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "Invalid URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Корзина",
                attachment_type=allure.attachment_type.PNG,
            )

    def remove_item(self):

        with allure.step("07. Удаление товара из корзины."):
            remove_item = self.driver.find_element("xpath", "//button[@id='remove-test.allthethings()-t-shirt-(red)']")
            checkout_button = self.driver.find_element("xpath", "//button[@id='checkout']")
            remove_item.click()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товар удален из корзины",
                attachment_type=allure.attachment_type.PNG,
            )
            checkout_button.click()

    def filling_in_checkout_fields(self):

        with allure.step("08. Заполнение полей чекаута."):
            first_name_field = self.driver.find_element("xpath", "//input[@id='first-name']")
            last_name_field = self.driver.find_element("xpath", "//input[@id='last-name']")
            zip_field = self.driver.find_element("xpath", "//input[@id='postal-code']")
            continue_button = self.driver.find_element("xpath", "//input[@id='continue']")
            first_name_field.clear()
            first_name_field.send_keys("Nikita")
            last_name_field.clear()
            last_name_field.send_keys("Tolstukhin")
            zip_field.clear()
            zip_field.send_keys("12345")

        with allure.step("09. Проверка заполнения полей чекаута"):
            first_name_field_actual_value = first_name_field.get_attribute("value")
            assert first_name_field_actual_value == "Nikita", "Ошибка в поле first_name"
            last_name_field_actual_value = last_name_field.get_attribute("value")
            assert last_name_field_actual_value == "Tolstukhin", "Ошибка в поле last_name"
            zip_field_actual_value = zip_field.get_attribute("value")
            assert zip_field_actual_value == "12345", "Ошибка в поле zip_field"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Поля чекаута заполнены корректно",
                attachment_type=allure.attachment_type.PNG,
            )
            continue_button.click()

    def go_to_second_checkout(self):

        with allure.step("10. Переход на второй чекаут"):
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Invalid URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Второй чекаут",
                attachment_type=allure.attachment_type.PNG,
            )

    def placing_an_order(self):

        with allure.step("11. Оформление заказа"):
            finish_button = self.driver.find_element("xpath", "//button[@id='finish']")
            finish_button.click()
            assert self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Invalid URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Заказ успешно оформлен",
                attachment_type=allure.attachment_type.PNG,
            )

    def return_to_home_page(self):

        with allure.step("12. Возврат на домашнюю страницу"):
            back_home_button = self.driver.find_element("xpath", "//button[@id='back-to-products']")
            back_home_button.click()
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Invalid URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Домашняя страница",
                attachment_type=allure.attachment_type.PNG,
            )

    def logout(self):

        with allure.step("13. Выход из системы"):
            wait = WebDriverWait(self.driver, 10, poll_frequency=1)
            burger_button = self.driver.find_element("xpath", "//button[@id='react-burger-menu-btn']")
            burger_button.click()
            logout_button = wait.until(
                EC.element_to_be_clickable(("xpath", "//a[@id='logout_sidebar_link']"))
            )
            logout_button.click()
            assert self.driver.current_url == "https://www.saucedemo.com/", "Invalid URL"
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница авторизации",
                attachment_type=allure.attachment_type.PNG,
            )

@allure.feature("Login")
@pytest.mark.usefixtures("driver")


class TestLoginWithIncorrectPassword:

    @pytest.mark.login_with_incorrect_password
    @allure.title("Login with incorrect password")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")

    def test_login_with_incorrect_password(self):
        with allure.step("01. Заполнение полей авторизации"):
            username_field = self.driver.find_element("xpath", "//input[@id='user-name']")
            password_field = self.driver.find_element("xpath", "//input[@id='password']")
            login_button = self.driver.find_element("xpath", "//input[@id='login-button']")
            username_field.clear()
            username_field.send_keys("standard_user")
            password_field.send_keys("")
            password_field.clear()
            password_field.send_keys("123")
            login_button.click()
            assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Invalid URL"
        with allure.step("02. Успешная авторизация."):
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Авторизация",
                attachment_type=allure.attachment_type.PNG,
            )
