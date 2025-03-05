import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Tests.login_test import fazer_login

def adicionar_item_ao_carrinho(browser):
    fazer_login(browser, "standard_user", "secret_sauce")

    try:
        dropdown_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )
        dropdown = Select(dropdown_element)

        filtros = [
            {"value": "az", "descricao": "Name (A to Z)"},
            {"value": "za", "descricao": "Name (Z to A)"},
            {"value": "lohi", "descricao": "Price (low to high)"},
            {"value": "hilo", "descricao": "Price (high to low)"},
        ]

        for filtro in filtros:
            print(f"Testando filtro: {filtro['descricao']}")

            dropdown.select_by_value(filtro["value"])

            dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))

            selected_option = dropdown.first_selected_option
            assert selected_option.get_attribute("value") == filtro["value"], f"Filtro {filtro['descricao']} não foi aplicado corretamente."

            WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
            )

            itens = browser.find_elements(By.CLASS_NAME, "inventory_item")

            nomes = []
            precos = []
            for item in itens:
                nome = item.find_element(By.CLASS_NAME, "inventory_item_name").text
                preco_texto = item.find_element(By.CLASS_NAME, "inventory_item_price").text
                preco = float(preco_texto.replace("$", ""))
                nomes.append(nome)
                precos.append(preco)

            if filtro["value"] == "az":
                assert nomes == sorted(nomes), "Itens não estão em ordem A to Z"
                print(nomes)
                print("Ordem A to Z verificada com sucesso!")
            elif filtro["value"] == "za":
                assert nomes == sorted(nomes, reverse=True), "Itens não estão em ordem Z to A"
                print(nomes)
                print("Ordem Z to A verificada com sucesso!")
            elif filtro["value"] == "lohi":
                assert precos == sorted(precos), "Preços não estão em ordem crescente"
                print(precos)
                print("Preços em ordem crescente verificados com sucesso!")
            elif filtro["value"] == "hilo":
                assert precos == sorted(precos, reverse=True), "Preços não estão em ordem decrescente"
                print(precos)
                print("Preços em ordem decrescente verificados com sucesso!")
    except Exception as e:
        print("Erro durante o teste:", e)


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