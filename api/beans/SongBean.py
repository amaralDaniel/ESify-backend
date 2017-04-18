from models import db
from models.Song import Song
from flask import json
from flask import redirect, url_for, escape, request


def __init__(self):
    pass



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def upload(data):

    try:
        from esify import session
        from AccountBean import get_user
        title = data.get('title')
        artist = data.get('artist')
        user = get_user(session["X-Auth-Token"])

        song = Song(title, artist, user)
        db.session.add(song)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False
