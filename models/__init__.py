from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from User import *
    from Song import *
    from Playlist import *

    db.drop_all()
    db.create_all()
