from functools import wraps
from flask import request, make_response, jsonify, current_app as app
import jwt


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        headers = request.headers
        # print("Request headers:\n" + str(headers))
        token = request.headers.get('x-token')
        if not token:
            return make_response(jsonify({'message': 'please provide token'}), 401)
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        except:
            return make_response(jsonify({'message': 'invalid token'}), 401)
        return f(*args, **kwargs)

    return decorated


def enforce_json_content(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.content_type and request.content_type != "application/json":
            return make_response(jsonify({'message': f"Content Type of {request.content_type} "
                                                     f"not supported. Only application/json is supported"}), 415)
        return f(*args, **kwargs)

    return decorated
