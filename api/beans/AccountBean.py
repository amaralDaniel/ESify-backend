from flask import json

from models import db
from models.User import User


def __init__(self, token):
    self.token = token
    self.user = self.get_user(token)

def get_user(token):
    user = User.query.filter_by(session_token=token).first_or_404()
    return user

def get_account(token):
    user = User.query.filter_by(session_token=token).first_or_404()

    data = {}
    data['email'] = user.email
    data['username'] = user.username

    json_data = json.dumps(data)
    return json_data


def update_account(token, data):

    try:
        user = User.query.filter(User.session_token == token).first_or_404()
        user.username = data.get('username')
        user.email = data.get('email')
        user.password = data.get('password')
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def delete_account(token):
    try:
        user = User.query.filter(User.session_token == token).first_or_404()
        db.session.delete(user)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False
