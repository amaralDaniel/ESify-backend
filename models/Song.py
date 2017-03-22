from esify import db


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), unique=True)
    artist = db.Column(db.String(120), nullable=False)
    uploader = db.Column(db.String(500), unique=True)

    def __init__(self, title, artist, uploader):
        self.title = title
        self.artist = artist
        self.uploader = uploader
