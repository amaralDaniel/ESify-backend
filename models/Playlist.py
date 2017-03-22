from esify import db

playlist_songs = db.Table('playlist_songs',db.Column('song_id',db.Integer,db.ForeignKey('Songs.id')),db.Column('playlist_id',db.Integer,db.ForeignKey('Playlists.id')))

class Playlist(db.Model):
    __tablename__ = 'Playlists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(1000))
    owner = db.Column(db.Integer, db.ForeignKey('Users.id'))
    playlist_songs = db.relationship('Song', secondary=playlist_songs,backref=db.backref('Playlists', lazy='dynamic'))

    def __init__(self, title, description,  owner, songs):
        self.title = title
        self.description = description
        self.owner = owner.id

    def __repr__(self):
            return '<Title %r>' % self.title
