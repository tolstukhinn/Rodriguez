import pytest
import allure
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@allure.epic("Accounts")
@allure.feature("Login")
@allure.story("Pages")
@pytest.mark.usefixtures("driver")
class TestPages:


    @pytest.mark.smoke
    @allure.title("Open login page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_login_page(self):
        with allure.step("Open login page. Step 1"):
            self.driver.get("https://demoqa.com/login")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Открытие login page",
                attachment_type=allure.attachment_type.PNG,
            )
        with allure.step("Check if login is working. Step 2"):
            assert self.driver.current_url == "https://demoqa.com/login", "Ошибка URL страницы входа"

    @pytest.mark.regression
    @allure.title("Open book page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_books_page(self):
        with allure.step("Open books page. Step 1"):
            self.driver.get("https://demoqa.com/books")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Открытие books page",
                attachment_type=allure.attachment_type.PNG,
            )
        with allure.step("Check if books are working. Step 2"):
            assert self.driver.current_url == "https://demoqa.com/books", "Ошибка URL страницы с книгами"

    @pytest.mark.profile
    @allure.title("Open profile page")
    @allure.severity(Severity.NORMAL)
    @allure.link(url="https://confluence.com", name="Documentation")
    def test_open_profile_page(self):
        with allure.step("Open profile page. Step 1"):
            self.driver.get("https://demoqa.com/profile")
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Открытие profile page",
                attachment_type=allure.attachment_type.PNG,
            )
        with allure.step("Check if profile page is working. Step 2"):
            assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка URL страницы профиля"