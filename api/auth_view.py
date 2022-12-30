from flask import Blueprint, request, make_response, jsonify, current_app as app
from flask_cors import cross_origin

from Helpers.decorators import enforce_json_content
import jwt
from models import User
from flask_bcrypt import Bcrypt
from extensions import *

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.post('/login')
@cross_origin(origin='*')
@enforce_json_content
def login():

    bd = request.json

    if bd and bd['username']:
        user = User.query.filter_by(username=bd['username']).first()
        if user:
            bcrypt = Bcrypt(app)
            if bcrypt.check_password_hash(pw_hash=user.password, password=bd['password']):
                token = jwt.encode({'user': bd['username'], 'user_id': user.id}, app.config['SECRET_KEY'])
                return make_response(jsonify({'responseCode': 200, 'token': token}), 200)
            else:
                return make_response(jsonify({'message': 'Authorization Failed'}), 401)
        else:
            return make_response(jsonify({'message': 'Authorization Failed, the username provided is not associated '
                                                     'with any account'}), 401)
    return make_response("Authorization Failed", 401)
