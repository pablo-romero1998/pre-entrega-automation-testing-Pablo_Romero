from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    time.sleep(3)  # Espera para asegurarse de que el navegador se haya abierto correctamente 

    

    try:
        # Open the login page
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(3)  # Espera para asegurarse de que la página haya cargado

        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario"

        print("Login exitoso, redirigido al inventario.")  
    
    # Maneja cualquier error que ocurra durante el proceso
    # Captura y registra cualquier excepción para evitar que el script se detenga abruptamente de login
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise 
    finally:
        # Close the browser
        driver.quit()