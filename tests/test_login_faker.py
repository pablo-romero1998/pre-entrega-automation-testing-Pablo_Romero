from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage

# Importamos Faker
from faker import Faker

# Inicializamos
fake = Faker()


@pytest.mark.parametrize("usuario,password,debe_funcionar", [
    (fake.user_name(),fake.password(length=8,special_chars=True,upper_case=True,lower_case=True,digits=True),False),
    (fake.user_name(),fake.password(),False),
])
def test_login_validation(login_in_driver,usuario,password,debe_funcionar):
    driver = login_in_driver
    LoginPage(driver).login_completo(usuario,password)

    if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    elif debe_funcionar == False:
        mensaje_error = LoginPage(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "No se mostró el mensaje de error esperado"

        