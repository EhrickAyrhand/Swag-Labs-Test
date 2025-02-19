import pytest
from selenium import webdriver
import time
@pytest.fixture
def browser():
    # Inicializa o navegador
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    time.sleep(5)
    driver.quit()