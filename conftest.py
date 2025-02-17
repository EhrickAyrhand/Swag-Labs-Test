import pytest
from selenium import webdriver
import time
@pytest.fixture
def browser():
    # Inicializa o navegador
    driver = webdriver.Chrome()
    yield driver
    # Fecha o navegador após o teste
    driver.quit()