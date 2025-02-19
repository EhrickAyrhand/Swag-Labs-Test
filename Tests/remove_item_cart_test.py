import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.login_test import fazer_login
from Tests.shopping_test import test_adicionar_item_ao_carrinho

def remover_itens_do_carrinho(browser):

    browser.get("https://www.saucedemo.com/cart.html")
