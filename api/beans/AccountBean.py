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
    json_data = json.loads(json.dumps(data))
    return json_data


def update_account(token, data):
    from hashlib import sha512
    try:
        user = User.query.filter(User.session_token == token).first_or_404()

        if( data.get('username')!=None):
            user.username = data.get('username')
        if( data.get('email')!=None):
            user.email = data.get('email')
        if( data.get('password')!=None):
            user.password = sha512(data.get('password')).hexdigest()
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
