import base64
from mimetypes import guess_extension, guess_type

from flask import make_response, Response, stream_with_context

from Helpers.Aux import *
from models import *
from extensions import db
# import zipfile


def upload_base64_image(file):
    filename = 'Files/'
    gs = generate_unique_string()
    if 'data:image' in file:
        extension = guess_extension(guess_type(file)[0])
        file = file[file.index('64,')+3:]
        filename += gs + extension
    if '.' not in filename:
        filename += gs + '.png'
    f = open(filename, "wb")
    f.write(base64.b64decode(file))
    f.close()
    file_size = get_file_size(filename)
    get_user_id_from_token()
    save_file_details(gs, filename, 'image', file_size, False)
    return gs
    # with zipfile.ZipFile('archive_zipfile.zip', 'w',
    #                      compression=zipfile.ZIP_BZIP2,
    #                      compresslevel=9) as zf:
    #     zf.write(filename, arcname=filename)


def upload_multipart_data():
    filename = app.config['STORAGE']
    gs = generate_unique_string()
    uploaded_file = request.files['file']
    filename += gs + uploaded_file.filename
    uploaded_file.save(filename)
    # get files info and save to table
    file_type = guess_file_type(uploaded_file.content_type)
    file_size = get_file_size(filename)
    get_user_id_from_token()
    save_file_details(file_id=gs, file_path=filename, file_type=file_type, file_size=file_size, is_compressed=False)
    return gs


def retrieve_file_base64(file_reference):
    if file_reference:
        filer = FileDetail.query.filter_by(file_id=file_reference).first()
        if filer:
            with open(filer.file_path, "rb") as img_file:
                encoded_file = base64.b64encode(img_file.read())
                filer.download_requests = filer.download_requests + 1
                db.session.commit()
                save_file_stats(filer.id, 'base64')
                return make_response(jsonify({'ResponseCode': 200, 'file': encoded_file.decode(encoding='utf-8')}))
        else:
            return make_response(jsonify({'ResponseCode': 404, 'ResponseMessage': f"File with the reference {file_reference} was not found"}))



def retrieve_the_file(file_reference):
    filename = FileDetail.query.filter_by(file_id=file_reference).first().file_path
    if filename:
        return Response(
            stream_with_context(read_file_chunks(filename)),
            headers={
                'Content-Disposition': f'attachment; filename={filename}'
            }
        )
    else:
        raise 'File Not Found'
        # return make_response(
        #     jsonify({'ResponseCode': 404, 'ResponseMessage': f"File with the reference {file_reference} was not found"}))
    pass


def read_file_chunks(path):
    with open(path, 'rb') as fd:
        while 1:
            buf = fd.read(app.config['CHUNK_SIZE'])
            if buf:
                yield buf
            else:
                break


def save_file_details(file_id, file_path, file_type, file_size, is_compressed):
    user_id = get_user_id_from_token()
    file_details = FileDetail(user_id=user_id, file_id=file_id, file_path=file_path, file_type=file_type,
                              file_size=file_size, is_compressed=is_compressed)
    db.session.add(file_details)
    db.session.commit()


def save_file_stats(file_id, download_mode):
    file_stat = FileStat(file_id=file_id, download_mode=download_mode)
    db.session.add(file_stat)
    db.session.commit()

