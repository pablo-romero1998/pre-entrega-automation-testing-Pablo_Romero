import requests
import pytest
from utils.logger import logger

# Test para verificar que se puede obtener la lista de usuarios
# @pytest.mark.skipif(reason="Skipping test temporarily")   
def test_get_echo():
    url = "https://postman-echo.com/get?foo=bar"
    logger.info(f"GET a {url}")
    response = requests.get(f"{url}")
    logger.info(f"Respuesta recibida con código de estado: {response.status_code}")
    assert response.status_code == 200

    data = response.json()
    
    logger.info(f"Validando el id dentro del usuario obtenido")
    assert data["args"]["foo"] == "bar"

# Test para verificar que se puede crear un nuevo usuario
# @pytest.mark.skipif(reason="Skipping test temporarily")  
def test_post_echo():
    url = "https://postman-echo.com/post"
    payload={
        "name": "Pablo",
        "job": "Tester"
    }
    logger.info(f"POST {url}")
    response = requests.post(url,json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["json"]["name"] == "Pablo"
    assert data["json"]["job"] == "Tester"

    # Test para verificar que se puede Eliminar un usuario existente
# @pytest.mark.skipif(reason="Skipping test temporarily") 
def test_delete_echo():
    url = "https://postman-echo.com/delete"
    logger.info(f"DELETE {url}")
    response = requests.delete(url)
    assert response.status_code == 200
    