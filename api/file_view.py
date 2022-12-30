import json

from flask import Blueprint, request, make_response, current_app as app, jsonify
import jwt
from Helpers.decorators import auth_required, enforce_json_content
from Helpers.file_processor import *

api = Blueprint('api', __name__, url_prefix='/api/file')


@api.post('upload-file')
@auth_required
def upload_file():
    if 'multipart/form-data' in request.content_type:
        result = upload_multipart_data()
        return make_response(jsonify({'ResponseCode': 200, 'FileReference': result}))
    elif 'application/json' in request.content_type:
        bd = request.json
        if bd:
            if bd['FileType'] == 'image':
                if bd['UploadMode'] == 'base64':
                    result = upload_base64_image(bd['File'])
                    return make_response(jsonify({'ResponseCode': 200, 'FileReference': result}))
                elif bd['UploadMode'] == 'file':
                    print(json.dumps(request.files))

    return make_response(jsonify({'ResponseCode': 200, 'FileReference': 'result'}))


@api.post('get-file')
@auth_required
@enforce_json_content
def retrieve_file():
    headers = request.headers
    # print("Request headers:\n" + str(headers))
    # download_choices = {
    #     base64: retrieve_file_base64,
    #     file: retrieve_file
    # }
    bd = request.json
    if bd:
        if bd['FileReference']:
            if bd['DownloadMode']:
                if bd['DownloadMode'] == 'base64':
                    return retrieve_file_base64(bd['FileReference'])
                elif bd['DownloadMode'] == 'file':
                    return retrieve_the_file(bd['FileReference'])
