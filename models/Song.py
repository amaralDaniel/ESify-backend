from models import db


class Song(db.Model):
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=False)
    uploader = db.Column(db.String(500), nullable=False)

    def __init__(self, title, artist, uploader):
        self.title = title
        self.artist = artist
        self.uploader = uploader


    def __repr__(self):
        return '<title %r>' % self.title
