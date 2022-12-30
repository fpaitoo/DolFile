import hashlib
import random
from datetime import datetime
import jwt
from flask import current_app as app, request, jsonify
import os
import math
from datetime import date, timedelta


def generate_unique_string():
    current_time = datetime.utcnow()
    random_digits = random.randint(999, 999999999)
    stg_to_hash = str(current_time) + str(random_digits)
    result = hashlib.md5(stg_to_hash.encode('utf-8')).hexdigest()
    return result
    # print(result)


def get_user_id_from_token():
    token = request.headers.get('x-token')
    if token:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        return data['user_id']


def get_file_size(file_path):
    stats = os.stat(file_path)
    return round(stats.st_size/1024, 2)  # return file size in kb


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def guess_file_type(conten_type):
    c_type = conten_type[:conten_type.index('/')]
    if c_type == 'application':
        return 'other'
    return c_type


def get_twelve_month_date():
    # Get the current date
    today = date.today()

    # Subtract 12 months from the current date
    twelve_months_ago = today - timedelta(days=365)
    timedelta()

    # Print the resulting date
    return str(twelve_months_ago)[:8] + '01'

