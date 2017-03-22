from esify import db
from models import user_playlists

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True)
    session_token = db.Column(db.String(256), unique=True)
    playlist = db.relationship('Playlist', secondary=playlist, backref=db.backref('Playlist', lazy='dynamic'))

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
        from utils import generate_token
        self.session_token = unicode(generate_token())
