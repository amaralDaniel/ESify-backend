
from passlib.hash import bcrypt
from models import db

def __init__(self):
    pass

def verify_token(self, token):
    from models import User
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
    from models.User import User

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try:
        user = User(email,  sha512(password).hexdigest(), username)
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False


def login(self, email, pwd):
    from models import User
    from esify import db, session
    import uuid
    from hashlib import sha512

    try:
        print pwd
        pwd = sha512(pwd).hexdigest()
        u = User.query.filter_by(email=email,password=pwd).first()
        if u is None:
            return False

        u.session_token = uuid.uuid4().hex
        db.session.commit()

        session["email"] = u.email
        session["X-Auth-Token"] = u.session_token

        return True
    except Exception as e:
        print e
        return False
