import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.login_test import fazer_login

def test_adicionar_item_ao_carrinho(browser):
    # Faz login
    fazer_login(browser, "standard_user", "secret_sauce")

    # Navega até a página de inventário
    browser.get("https://www.saucedemo.com/inventory.html")

    # Adiciona um item ao carrinho
    item = browser.find_element(By.CLASS_NAME, "btn_primary")
    item.click()

    # Verifica se o item foi adicionado ao carrinho
    wait = WebDriverWait(browser, 10)
    carrinho = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert "1" in carrinho.text  # Verifica se o número de itens no carrinho é 1

    # Atualiza a referência ao botão após o primeiro clique
    item = browser.find_element(By.CLASS_NAME, "btn_secondary")  # Localiza o botão novamente

    # Tenta adicionar o mesmo item novamente
    item.click()

    # Verifica se o carrinho ainda contém apenas uma unidade do item
    assert "1" in carrinho.text  # O número de itens no carrinho ainda deve ser 1

    # Verifica se o botão "Add to cart" foi alterado para "Remove"
    assert item.text == "Remove"  # Verifica se o texto do botão mudou