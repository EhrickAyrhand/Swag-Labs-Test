from selenium.webdriver.common.by import By
from Tests.shopping_test import adicionar_item_ao_carrinho
import time

def remover_itens_do_carrinho(browser):
    
    adicionar_item_ao_carrinho(browser)
    
    browser.get("https://www.saucedemo.com/cart.html")
    
    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    
    remove_buttons = []
    
    for item in cart_items:
        price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
        price_text = price_element.text
        
        price = float(price_text.replace("$", ""))
        
        if price > 15.99:
            remove_button = item.find_element(By.CLASS_NAME, "cart_button")
            remove_buttons.append(remove_button)
    
    if remove_buttons:
        for button in remove_buttons:
            time.sleep(2)
            button.click()
    else:
        print("Nenhum item com preço acima de 15.99 encontrado no carrinho.")
    
    total_price = 0.0

    remaining_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    for item in remaining_items:
        price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
        price_text = price_element.text
        price = float(price_text.replace("$", ""))
        assert price <= 15.99, f"Item com preço {price} ainda está no carrinho."
        print(f"no carrinho há os seguintes valores de itens {price}")

        total_price += price

    print(f"Valor final é {total_price}")