import requests
import random
from bs4 import BeautifulSoup

# Funccion para rotar User-Agent
def rotar_user_agent():
    user_agents = [
    'Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36',  # chrome
    'Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36',  # chrome
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0',  # firefox
    'Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.91 '
     'Safari/537.36',  # chrome
    'Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/62.0.3202.89 '
     'Safari/537.36',  # chrome
    'Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/63.0.3239.108 '
     'Safari/537.36',  # chrome
    ]
    return random.choice(user_agents)


# Función para obtener los datos de un producto en Amazon
def obtener_datos(url):
    headers = {
        'User-Agent': rotar_user_agent(),}
    # Realizar la solicitud HTTP con el User-Agent
    response = requests.get(url, headers=headers)
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        # Obtener el título del producto
        titulo_producto = soup.find('span', id='productTitle').text.strip()
        # Obtener el precio del producto quitando el símbolo de la moneda
        precio_producto = soup.find('span', class_='a-offscreen').text[:-1].strip()
        # Obtener la URL de la imagen
        imagen_producto = soup.find('img', id='landingImage')['src']
        # Create an object with the obtained values
        producto = {
            'titulo': titulo_producto,
            'precio': precio_producto,
            'imagen': imagen_producto
        }
        print(producto)
        return producto

    else:
        return {'error': f"Error al obtener la pagina: {response.status_code}"}


        
# URL de ejemplo
#url_ejemplo = "https://www.amazon.es/Logitech-Iluminaci%C3%B3n-Personalizable-Programables-Ultra-ligero/dp/B07W5JKFQC/?_encoding=UTF8&ref_=pd_gw_glx_wl_gw_glx_0"

# Llamar a la función para obtener los datos
#obtener_datos(url_ejemplo)
