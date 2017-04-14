class AccountBean(object):

    def __init__(self, token):
        self.token = token
        self.user = self.get_user()

    def get_user(self):
        from models import User
        user = User.query.filter_by(session_token=self.token).first()
        return user

    def delete_account(self):
        try:
            db.session.delete(self.user)
            db.session.commit()
            return True
        except Exception as e:
            print e
            return False
