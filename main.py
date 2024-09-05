from app import crear_app
from config.configuracion import Config

app = crear_app()
config_instance = Config()
config_instance.config()

if __name__  == "__main__":
    app.run( debug=True,port=config_instance.PORT)