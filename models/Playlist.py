from esify import db

playlist_songs = db.Table('user_playlists',
                    db.Column("user_id",db.Integer,db.ForeignKey('user_id')),
                    db.Column("playlist_id",db.Integer,db.ForeignKey('playlist_id'))
                )

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    owner = db.Column(db.Integer, db.ForeignKey('company.id'))
    songs = db.relationship('Songs', secondary=playlist_songs,
                                       backref=db.backref('songs', lazy='dynamic'))



    def __init__(self, title, description,  owner, songs):
        self.title = title
        self.description = description
        self.owner = owner.id
