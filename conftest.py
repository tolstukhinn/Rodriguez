from collections import namedtuple
import pytest
from faker import Faker
from urllib3 import request
faker = Faker()
from selenium import webdriver


@pytest.fixture(name="WDI")
def driver(request):

    driver = webdriver.Chrome()
    request.cls.driver = driver

@pytest.fixture(autouse=True)
def driver2(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    print("Before")
    yield
    print("After")
    driver.quit()