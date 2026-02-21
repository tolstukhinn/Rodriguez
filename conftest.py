import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(autouse=True)
def setup_environment():

    properties = {
        "STAGE": os.environ["STAGE"],
        "BROWSER": os.environ["BROWSER"],
        "PYTHON": os.environ["PYTHON"],
        "MR": os.environ["MR"]
    }
    with open("allure-results/environment.properties", 'w') as file:
        for key, value in properties.items():
            file.write(f"{key}={value}\n")


#  $env:STAGE="stage1"; $env:BROWSER="chrome"; $env:PYTHON="3.13"; $env:MR="https://gitlub.sber.ru/SPG-2517"; pytest exploring_pytest\test_allure.py --alluredir=allure-results