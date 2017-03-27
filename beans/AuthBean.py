class AuthBean(object):
    from passlib.hash import bcrypt

    def __init__(self):
        pass

    def register(self, email, password, username):
        from models import *
        from esify import db
        from hashlib import sha512

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
            print pwd
            u = User.query.filter_by(email=email,password=pwd).first()
            # print u.username
            print u.password
            # print u.email
            if u is None:
                print "false"
                return False

            u.session_token = uuid.uuid4().hex
            db.session.commit()

            session["email"] = u.email
            session["X-Auth-Token"] = u.session_token

            return True
        except Exception as e:
            print e
            return False
