from app.itop_peticion import itop_request

def register_routes(app): 
    app.register_blueprint(itop_request, url_prefix='/itop')