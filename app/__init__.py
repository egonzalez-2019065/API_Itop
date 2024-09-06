from flask import Flask
from config.configuracion import Config
from flask_cors import CORS
from rutas import register_routes


def crear_app():
    # Instancia Flask 
    app = Flask(__name__)

    # Configuración de la aplicación 
    app.config.from_object(Config)

    # Configuración de CORS 
    CORS(app)

    # Configuración de la rutas 
    register_routes(app)
    
    # De prueba
    @app.route('/')
    def home():
        return 'Holaaaaa, esta es una pruebaa'

    return app

