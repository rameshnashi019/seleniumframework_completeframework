import pytest
from selenium import webdriver


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    ch_driver = webdriver.Chrome()
    ch_driver.maximize_window()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()