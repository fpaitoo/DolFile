from flask import current_app as app

from extensions import db
from datetime import datetime
from Helpers import Aux
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now())


class FileDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('FileDetail', lazy=True))
    file_id = db.Column(db.String, nullable=False, default=Aux.generate_unique_string())
    file_path = db.Column(db.String, nullable=True)
    file_type = db.Column(db.String, nullable=True)
    file_size = db.Column(db.Integer, nullable=True)
    download_requests = db.Column(db.Integer, nullable=False, default=0)
    is_compressed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=True, default=datetime.now())


class FileStat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, nullable=True)
    download_mode = db.Column(db.String, nullable=True)
    accessed_at = db.Column(db.DateTime, nullable=True, default=datetime.now())


