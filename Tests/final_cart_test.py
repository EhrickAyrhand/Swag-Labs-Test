import pytest
from selenium.webdriver.common.by import By
from Tests.login_test import fazer_login
from Tests.shopping_test import adicionar_item_ao_carrinho
from Tests.remove_item_test import remover_itens_do_carrinho
import time

def test_finalizar_compra_carrinho(browser):
    remover_itens_do_carrinho(browser)

    browser.get("https://www.saucedemo.com/cart.html")

    btn_finalizar = browser.find_element(By.CLASS_NAME, "btn_action ")

    btn_finalizar.click()

    #Campo de nome

    #Campo de endereço

    #Campo de Postal Code

    #Botão de confirmação

    #Botão de finalização

    #Verificação de erro
    