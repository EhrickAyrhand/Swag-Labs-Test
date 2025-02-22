import pytest
from selenium.webdriver.common.by import By
from Tests.login_test import fazer_login
from Tests.shopping_test import adicionar_item_ao_carrinho
from Tests.remove_item_test import remover_itens_do_carrinho
import time


dados_teste = [
    {"nome": "Hallana", "sobrenome": "Velho", "postal": 1234567}
]

@pytest.mark.parametrize("dados", dados_teste)
def test_finalizar_compra_carrinho(browser, dados):
    remover_itens_do_carrinho(browser)

    browser.get("https://www.saucedemo.com/cart.html")

    btn_finalizar = browser.find_element(By.CLASS_NAME, "btn_action ")

    btn_finalizar.click()

    primeiro_nome = browser.find_element(By.ID, "first-name")
    ultimo_nome = browser.find_element(By.ID, "last-name")
    postal_code = browser.find_element(By.ID, "postal-code")
    btn_continue = browser.find_element(By.ID, "continue")
 
    primeiro_nome.clear()
    ultimo_nome.clear()
    postal_code.clear()
    time.sleep(5)
    primeiro_nome.send_keys(dados["nome"])
    time.sleep(5)
    ultimo_nome.send_keys(dados["sobrenome"]) 
    time.sleep(5)
    postal_code.send_keys(dados["postal"])
    time.sleep(5)

    btn_continue.click()