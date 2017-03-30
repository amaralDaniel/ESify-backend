class UserPlaylistBean(object):

    def __init__(self, token):
        self.token = token
        self.user = self.get_user()


    def get_user(self):
        from models import User
        user = User.query.filter_by(session_token=self.token).first()
        return user

    def get_user_playlists(self):
        return self.user.playlists
