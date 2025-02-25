from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Função para fazer login
def fazer_login(browser, username, password):
    browser.get("https://www.saucedemo.com")
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()

    expected_url = "https://www.saucedemo.com/inventory.html"
    try:
        WebDriverWait(browser, 10).until(EC.url_to_be(expected_url))
        print(f"✅ Login bem-sucedido para {username}! Redirecionado para a URL correta.")
    except:
        pytest.fail(f"❌ Falha no login para {username}. URL atual: {browser.current_url}")

    time.sleep(2)

dados_teste = [
    {"nome": "standard_user", "senha": "secret_sauce"},
]

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()