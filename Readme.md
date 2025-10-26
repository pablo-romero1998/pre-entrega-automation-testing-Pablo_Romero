# Pruebas de Automatización - SauceDemo

Este proyecto contiene pruebas automatizadas para  **SauceDemo**, utilizando  **Python** y **Selenium WebDriver**.

## Funcionalidades 
Los tests automatizados verifican las siguientes áreas:

1.  **Login:** Inicio de sesión exitoso con credenciales válidas.

2.  **Inventory (Inventario):** Visualización correcta de productos después del login.
3.  **Carrito (Cart):** Agregar y verificar que los productos se añaden correctamente al carrito.

## para ejecion de pruebas 

Para ejecutar las pruebas del proyecto se deberá tener instaladas las dependencias  `selenium`, `pytest`, `webdriver en caso de usar chrome`

`pasos`
1- Descargar pytest
2- Descargar webdriver
3- Importar en cada archivo su correcto modulo.


# Ejemplo de ejecución si usas pytest
pytest -v
py -m pytest test_login.py

# tambien se puede correr el programa directamente de VSC'run_tests.py'
run_tests.py