from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver:WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
        
    driver.quit()