import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.login_test import fazer_login
from Tests.shopping_test import adicionar_item_ao_carrinho
import time

def test_remover_itens_do_carrinho(browser):
    fazer_login(browser, "standard_user", "secret_sauce")
    adicionar_item_ao_carrinho(browser)
    
    browser.get("https://www.saucedemo.com/cart.html")
    
    remove_buttons = browser.find_elements(By.CLASS_NAME, "cart_button")
    for button in remove_buttons:
        time.sleep(3)
        button.click()
        time.sleep(3)
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 0, "O carrinho não está vazio após remover os itens"