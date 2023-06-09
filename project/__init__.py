import os
from flask import Flask
from flask_login import LoginManager
from flask_security import Security,SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

#Creamos instancia de SQLAlchemy
db = SQLAlchemy()
from .models import User,Role
#Creamos un objeto de SQLAlchemyUserDatastore
userDataStore=SQLAlchemyUserDatastore(db,User,Role)

#Método de inicio de la aplicación
def create_app(test_config=None):
    #Creamos nuestra aplicación de Flask
    app = Flask(__name__)

    #Creamos la configuración de la aplicación
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1/flasksecurity"
    app.config['SECURITY_PASSWORD_HASH'] = 'pbkdf2_sha512'
    app.config['SECURITY_PASSWORD_SALT'] = 'secretsalt'

    db.init_app(app)
    #Método para crear la BD en la primera petición
    @app.before_first_request
    def create_all():
        db.create_all()
    
    #Conectando los modelos de Flask-security usando SQLAlchemyUserDatastore
    security=Security(app,userDataStore)

    #Registramos dos Blueprints 
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .productos import productos as productos_blueprint
    app.register_blueprint(productos_blueprint)

    from .producto import producto as producto_blueprint
    app.register_blueprint(producto_blueprint)

    return app

