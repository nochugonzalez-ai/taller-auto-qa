from playwright.sync_api import Page
import pytest

def test_login_exitoso_tienda(page: Page):
    print("\n[WEB TEST] Iniciando prueba de interfaz de usuario...")
    
    # 1. El navegador navega automáticamente a la url
    page.goto("https://www.saucedemo.com/")
    
    # 2. Localizamos los elementos de la pantalla e interactuamos con ellos
    # Escribimos el usuario de pruebas que nos da la página
    page.fill("input[data-test='username']", "standard_user")
    
    # Escribimos la contraseña
    page.fill("input[data-test='password']", "secret_sauce")
    
    # Hacemos clic en el botón de Login
    page.click("input[data-test='login-button']")
    
    # 3. LA PRUEBA DE QA: Validamos si cambiamos de página a la tienda de productos
    # Al iniciar sesión, la URL debe cambiar e incluir '/inventory.html'
    url_actual = page.url
    print(f"[INFO] URL alcanzada tras el login: {url_actual}")
    
    assert "/inventory.html" in url_actual, f"Error: El login falló, nos quedamos en {url_actual}"
    print("✓ PASÓ: El login fue exitoso y entramos a la tienda.")
# Código basura de prueba para simular un descuido:
exec("print('Hola, soy una vulnerabilidad')")
