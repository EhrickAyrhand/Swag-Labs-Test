from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

dados_teste = [
    {"nome": "João Silva", "senha": "123456789"},
    {"nome": "standard_user", "senha": "secret_sauce"},
]

@pytest.fixture
def driver():
    driver = webdriver.Chrome() 
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    yield driver 
    driver.quit()

@pytest.mark.parametrize("dados", dados_teste)
def test_cadastro_newsletter(driver, dados):
    wait = WebDriverWait(driver, 10)

    campo_nome = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    campo_senha = driver.find_element(By.ID, "password")
    botao_envio = driver.find_element(By.ID, "login-button")

    campo_nome.clear()
    campo_senha.clear()

    campo_nome.send_keys(dados["nome"])
    campo_senha.send_keys(dados["senha"]) 

    botao_envio.click()

    try:
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "right_component")
        ))
    except:
        pytest.fail("❌ Nenhuma mensagem de resposta encontrada")

    time.sleep(5)