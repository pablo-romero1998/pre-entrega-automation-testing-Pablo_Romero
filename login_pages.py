from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    #URL de la página de login
    URL = "https://saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver    
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def ingresar_usuario(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self

    def ingresar_pass(self, password):
        input = self.driver.find_element(*self._PASS_INPUT)
        input.send_keys(password)
        return self
    
    def hacer_click_button(self):
        boton = self.driver.find_element(*self._LOGIN_BUTTON)
        boton.click()
        return self
    
    def login_completo(self, usuario, password): 
        self.ingresar_usuario(usuario)
        self.ingresar_pass(password)
        self.hacer_click_button()
        return self
    

