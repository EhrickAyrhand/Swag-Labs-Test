import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.login_test import fazer_login

def adicionar_item_ao_carrinho(browser):
    fazer_login(browser, "standard_user", "secret_sauce")

    wait = WebDriverWait(browser, 10)
    botoes_adicionar = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_primary")))

    assert len(botoes_adicionar) >= 4, "Não há itens suficientes para adicionar ao carrinho."

    itens_aleatorios = random.sample(botoes_adicionar, 4)

    for item in itens_aleatorios:
        item.click()

    carrinho = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert carrinho.text == "4", f"O carrinho deveria ter 4 itens, mas tem {carrinho.text}."