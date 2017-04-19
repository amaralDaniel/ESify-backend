from models import db


class Song(db.Model):
    __tablename__ = 'Songs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=False)
    album = db.Column(db.String(120), nullable=False)
    release_year = db.Column(db.Integer,nullable=False)
    path_to_file = db.Column(db.String(120), nullable=False)
    uploader = db.Column(db.String(500), nullable=False)

    def __init__(self, title, artist,album,release_year,path_to_file,uploader):
        self.title = title
        self.artist = artist
        self.album = album
        self.release_year = release_year
        self.path_to_file = path_to_file
        self.uploader = uploader


    def __repr__(self):
        return '<title %r>' % self.title
