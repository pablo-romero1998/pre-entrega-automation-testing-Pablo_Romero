from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_valid_credentials(login_in_driver):
    driver = login_in_driver

    try:
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"
        print("Login exitoso, redirigido al inventario.")  
    except Exception as e:
        print(f"Error en test_login_valid_credentials: {e}")
        raise
    finally:
        driver.quit()
