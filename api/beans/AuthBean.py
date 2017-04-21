from passlib.hash import bcrypt
from models import db
from models.User import User

from flask import redirect, url_for, escape, request


def __init__(self):
    pass


def verify_token(token):
    try:
        user = User.query.filter_by(session_token=token).first()
        if user is None:
            return False
        else:
            return True
    except Exception as e:
        return False


def register(data):
    from hashlib import sha512

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try:
        user = User(email, sha512(password).hexdigest(), username)
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False


def login(data):
    import uuid
    from hashlib import sha512
    from esify import session

    try:
        email = data.get('email')
        password = data.get('password')

        pwd = sha512(password).hexdigest()
        u = User.query.filter_by(email=email, password=pwd).first()
        if u is None:
            return False

        u.session_token = uuid.uuid4().hex
        db.session.commit()

        session['logged_in'] = True
        session["X-Auth-Token"] = u.session_token
        return True
    except Exception as e:
        print e
        return False


def logout():
    from esify import session

    try:
        session.pop('logged_in', None)
        return True
    except Exception as e:
        print e
        return False
