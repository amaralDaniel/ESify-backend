from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from models import User, Song, Playlist

    db.drop_all()
    db.create_all()
