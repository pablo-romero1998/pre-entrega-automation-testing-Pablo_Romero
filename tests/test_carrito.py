from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_agregar_producto_al_carrito():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # 1. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # **Agregar un producto y verificar el contador del carrito**
    
    # 2. Localizar el primer producto (es mejor usar un localizador más específico)
    producto = driver.find_elements(By.CLASS_NAME, "inventory_item")
    
    # 3. Hacer clic en el botón de agregar del PRIMER producto
    # El botón de agregar de SauceDemo tiene la clase 'btn_primary'
    producto[0].find_element(By.TAG_NAME, "button").click()

    # 4. Verificar el badge del carrito
    # El localizador correcto para el badge es por su clase o CSS Selector
    cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    
    # 5. La aserción (El test pasa si el badge existe y tiene el texto "1")
    assert cart_badge.text == "1", "El contador del carrito no mostró '1'."

    # 6. Siempre cerrar el navegador al finalizar la prueba
    driver.quit()