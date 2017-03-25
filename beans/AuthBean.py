class AuthBean(object):
    def __init__(self):
        pass

    def register(self, email, password, username):
        from models import *
        from esify import db
        from hashlib import sha512

        try:
            user = User(email, sha512(password).hexdigest(), username)
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as e:
            print e
            return False
