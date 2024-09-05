from flask import Blueprint, jsonify
from .get_json import get_json
from config.configuracion import Config
import requests


# Define el Blueprint 
itop_request = Blueprint('itop_request', __name__)

@itop_request.route('/insert_request')
def process_json():
    config_instance = Config()
    config_instance.config()

    api_url = config_instance.API_URL
    api_itop = config_instance.ITOP_URL

    try:
        data = get_json() 

        # Manejar la respuesta 
        response = requests.post(api_url)
        if response.status_code != 200:
            return jsonify({'error': 'Error al realizar la conexión al API'})
        
        # Extraer el token de la respuesta 
        token = response.json().get('token')
        if not token: 
            return jsonify({'Error': 'Error al obtener el token'})
        
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

        # Enviar los datos a Itop 
        itop_response = requests.post(api_itop, json=data, headers=headers)

        # Verificar la respuesta de iTop
        if itop_response.status_code == 200:
            return jsonify({'success': 'Los datos fueron enviados correctamente a iTop'}), 200
        else:
            return jsonify({'error': 'Error al enviar los datos a iTop', 'details': itop_response.text}), 500

    except FileNotFoundError as e:
        return jsonify({'El archivo no fue encontrado': e}), 404
    except ValueError as e:
        return jsonify({'El archivo no contiene el contenido esperado': e}), 500