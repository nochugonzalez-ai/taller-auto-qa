import requests

# Definimos la URL base como una constante del proyecto
URL_BASE = "https://jsonplaceholder.typicode.com/posts/1"

def test_codigo_de_respuesta_es_200():
    """Validar que el servidor esté en línea y responda con éxito (200 OK)"""
    respuesta = requests.get(URL_BASE)
    
    # Assert evalúa si la condición se cumple. Si no, lanza el error con el texto asignado.
    assert respuesta.status_code == 200, f"Error: Se esperaba 200 pero se recibió {respuesta.status_code}"

def test_id_de_usuario_es_correcto():
    """Validar que el recurso devuelto pertenezca al usuario ID 1"""
    respuesta = requests.get(URL_BASE)
    datos = respuesta.json()
    
    id_usuario = datos.get("userId")
    
    # Validamos que los datos dentro del JSON sean los correctos
    assert id_usuario == 1, f"Error: El userId esperado era 1, pero se obtuvo {id_usuario}"
