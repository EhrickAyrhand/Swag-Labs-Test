import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.login_test import fazer_login

def adicionar_item_ao_carrinho(browser):
    # Faz login
    fazer_login(browser, "standard_user", "secret_sauce")

    # Navega até a página de inventário

    # Localiza todos os botões "Add to cart"
    browser.get("https://www.saucedemo.com/inventory.html")
    wait = WebDriverWait(browser, 10)
    botoes_adicionar = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))

    # Verifica se há pelo menos 4 itens disponíveis
    assert len(botoes_adicionar) >= 4, "Não há itens suficientes para adicionar ao carrinho."

    # Seleciona 4 itens aleatórios
    itens_aleatorios = random.sample(botoes_adicionar, 4)

    # Adiciona os 4 itens ao carrinho
    for item in itens_aleatorios:
        item.click()

    # Verifica se os itens foram adicionados ao carrinho
    carrinho = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert carrinho.text == "4", f"O carrinho deveria ter 4 itens, mas tem {carrinho.text}."