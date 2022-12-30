import sys

# setting path
sys.path.append('./')

from flask import Flask, request
import json

from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from api.file_view import api
from api.auth_view import auth
from dashboard.login import logins
from dashboard.dashboard import dashboard
from extensions import db
from models import User, FileDetail
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from Helpers import Aux


def create_app():
    app = Flask(__name__)
    login_manager = LoginManager()
    login_manager.login_view = 'login.index'
    CORS(app)
    app.config.from_file('config.json', json.load)
    app.register_blueprint(api)
    app.register_blueprint(auth)
    app.register_blueprint(logins)
    app.register_blueprint(dashboard)
    app.register_blueprint(get_and_initialize_swagger_ui(app))
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        print(f"USER ID {user_id}")
        # user = User.get(user_id)
        if user_id:
            return User.query.filter_by(id=user_id).first()
        else:
            return None

    with app.app_context():
        # db.drop_all()
        # db.create_all()
        # create_user(app)
        pass
    return app


def create_user(app):
    bcrypt = Bcrypt(app)
    password = bcrypt.generate_password_hash(password='password', rounds=10).decode('UTF-8')
    user = User(username='admin', password=password, name='Administrator', is_active=True)
    db.session.add(user)
    db.session.commit()


def get_and_initialize_swagger_ui(app):
    swaggerui_blueprint = get_swaggerui_blueprint(
        app.config['SWAGGER_URL'],  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        app.config['API_URL'],
        config={  # Swagger UI config overrides
            'app_name': "Test application"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )
    return swaggerui_blueprint
