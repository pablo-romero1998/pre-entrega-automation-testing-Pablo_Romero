from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_inventory_page(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No se encontraron productos en la página de inventario"
        
    except Exception as e:
        print(f"Error en test_inventory_page: {e}")
        raise    
    finally:
        driver.quit()

