import bcrypt
import flask
from flask import Blueprint, render_template, request, current_app as app
from flask_login import login_manager, login_user, current_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from extensions import db

from models import User, FileDetail
from flask_bcrypt import Bcrypt

logins = Blueprint('login', __name__)


@logins.get('/login/')
def index():
    # print(FileDetail.query.count())
    return render_template('login.html')


@logins.post('/login/')
def login():
    error = None
    # print(request.form['username'])
    # print('here 1')
    if request.method == 'POST':
        # print('here 2')
        if request.form['username']:
            user = User.query.filter_by(username=request.form['username']).first()
            if user:
                bcrypt = Bcrypt(app)
                if bcrypt.check_password_hash(pw_hash=user.password, password=request.form['password']):
                    login_user(user)
                    return flask.redirect(flask.url_for('dashboard.index'))
                else:
                    error = 'Invalid Credentials. Please try again.'
            else:
                error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)
    else:
        # print('testing')
        return render_template('login.html')


@logins.route("/logout/")
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('login.index'))


@logins.route('/user-management', methods=('GET', 'POST'))
@login_required
def user_management():
    form = CreateUserForm()
    message = ''
    if form.validate_on_submit():
        my_bcrypt = Bcrypt(app)
        user = User.query.filter_by(username=form.username.data).first()
        if my_bcrypt.check_password_hash(pw_hash=user.password, password=form.current_password.data):
            password = my_bcrypt.generate_password_hash(password=form.new_password.data, rounds=10).decode('UTF-8')
            user.password = password
            user.name = form.name.data
            db.session.commit()
            message = 'User details has been updated successfully'
        else:
            message = 'The current password provided is invalid'

    return flask.render_template('user_management.html', form=form, message=message)


class CreateUserForm(FlaskForm):
    username = StringField(label='Username',
                           validators=[DataRequired(),
                                       Length(max=64)])
    name = StringField(label='Full Name',
                       validators=[DataRequired(),
                                   Length(max=64)])
    current_password = PasswordField(label='Current Password',
                                     validators=[DataRequired(),
                                                 Length(min=6,
                                                        message='Password should be at least %(min)d characters long')])
    new_password = PasswordField(label='New Password',
                                 validators=[DataRequired(),
                                             Length(min=8,
                                                    message='Password should be at least %(min)d characters long')])
    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[DataRequired(message='*Required'),
                    EqualTo('new_password', message='Both password fields must be equal!')])

    submit = SubmitField(label='Submit')

    def validate_current_password(self, current_password):
        my_bcrypt = Bcrypt(app)
        user = User.query.filter_by(username=self.username.data).first()
        if not my_bcrypt.check_password_hash(pw_hash=user.password, password=self.current_password.data):
            raise ValidationError("The current password provided is invalid")
