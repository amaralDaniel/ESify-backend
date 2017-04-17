from datetime import datetime
from models import db
from models.Playlist import Playlist
import uuid
from passlib.hash import bcrypt

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.String(300), primary_key=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(120), unique=True)
    session_token = db.Column(db.String(256), unique=True)
    playlists = db.relationship('Playlist',backref='user',lazy="dynamic")

    def __init__(self, email, password, username):
        self.id = uuid.uuid4().hex
        self.email = email
        self.password = password
        self.username = username



    # def verify_password(self, password):
    #     pwhash = bcrypt.hashpw(password, self.password)
    #     return self.password == pwhash

    def __repr__(self):
        return '<username %r, >' % self.username
