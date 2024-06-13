from flask import Flask
from utils.db import db

def create_app():
    app = Flask(__name__)

    # Parámetros de la base de datos
    user = 'root'
    password = 'admin'
    table = 'productsdb'

    # Configuración de SQLAlchemy (base de datos)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{user}:{password}@localhost/{table}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de la base de datos
    db.init_app(app)

    # Registro de los blueprints
    from routes.products import products
    app.register_blueprint(products)

    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
    
    return app
