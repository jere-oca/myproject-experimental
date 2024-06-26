from flask import Flask
from utils.db import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Parámetros de la base de datos
    user = 'root'
    password = 'password'
    table = 'products'

    # Configuración de SQLAlchemy (base de datos)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{user}:{password}@localhost/{table}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de la base de datos
    migrate = Migrate(app, db)

    # Registro de los blueprints
    from routes.productos import products
    from routes.marcas import marcas

    app.register_blueprint(products)
    app.register_blueprint(marcas, url_prefix='/marcas')

    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
    
    return app
