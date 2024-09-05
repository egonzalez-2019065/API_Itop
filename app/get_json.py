from flask import jsonify
import os
import json

def get_json(): 
    directorio_usuario = os.path.expanduser('~')
    ruta = None 

    # Manejo de diferentes rutas según el idioma de la computadora 
    if os.path.exists(os.path.join(directorio_usuario, 'Documents')):
        ruta = os.path.join(directorio_usuario, 'Documents', 'data')
    elif os.path.exists(os.path.join(directorio_usuario, 'Documentos')):
        ruta = os.path.join(directorio_usuario, 'Documentos', 'data')
    
    if not ruta: 
        return jsonify({'error': 'No se encontró la carpeta del archivo JSON'}), 404
    
    # Obteniendo la ruta del archivo 
    archivo_json = os.path.join(ruta, 'data.json')

    # Verificar si existe el archivo json 
    if not os.path.exists(archivo_json):
        return jsonify({'error': 'No se pudo leer el JSON'}), 404
    
    # Leer el archivo JSON
    with open(archivo_json, 'r') as archivo: 
        try:
            data = json.load(archivo)
            return data 
        except json.JSONDecodeError:            
            return jsonify({'error': 'No se pudo leer el JSON'}), 404
 
