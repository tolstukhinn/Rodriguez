
from selenium import webdriver


class TestExample:

    def setup_method(self):
        print("setup method called")
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Invalid URL"

    def teardown_method(self):
        print("teardown method called")
        self.driver.quit()


    # def test_login(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://demoqa.com/login")
    #     assert driver.current_url == "https://demoqa.com/login", "Invalid URL"