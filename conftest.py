import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

PORTAL_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

@pytest.fixture
def driver() -> webdriver.Chrome:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(PORTAL_URL)
    yield driver
    driver.close()
