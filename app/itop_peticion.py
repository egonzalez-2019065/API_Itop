from flask import Blueprint, jsonify, request
from config.configuracion import Config
import requests
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define el Blueprint 
itop_request = Blueprint('itop_request', __name__)

@itop_request.route('/insert_request', methods=['POST'])
def process_json():
    config_instance = Config()
    config_instance.config()

    api_itop = config_instance.ITOP_URL  # API de iTop para insertar datos

    try:
        # Obtener los datos del cuerpo de la solicitud
        request_data = request.get_json()

        # Obtener los datos del header 
        request_token = request.headers.get('Authorization')
        if request_token.startswith('Bearer '):
            request_token = request_token[len('Bearer '):]
        
        # Extraer el token y los datos desde la solicitud
        token = request_token
        data = request_data

        if not token:
            return jsonify({'error': 'Token no proporcionado'}), 400
            

        if not data:
            return jsonify({'error': 'Datos no proporcionados'}), 400

        # Definir los headers con el token
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }


        # Enviar los datos a la API de iTop
        itop_response = requests.post(api_itop, json=data, headers=headers)

        # Verificar la respuesta de iTop
        if itop_response.status_code == 200:
            return jsonify({'success': 'Los datos fueron enviados correctamente a iTop'}), 200
        else:
            logging.info(data)
            return jsonify({'error': 'Error al enviar los datos Itop', 'details': itop_response.text}, data), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error en la petición HTTP: {str(e)}'}), 500
