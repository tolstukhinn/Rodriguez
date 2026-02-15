import pytest
from selenium import webdriver


class TestLogin:    # Название тестового класса

    def setup_method(self):
        self.driver = webdriver.Chrome()
    @pytest.mark.smoke
    def test_open_login_page(self):     # Тест пройдет
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Ошибка"

    @pytest.mark.smoke
    def test_open_books_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books", "Ошибка в books_page"
    @pytest.mark.profile
    def test_open_profile_page(self):     # Тест упадет
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile", "Ошибка в profile_page"

    def teardown_method(self):
        self.driver.close()