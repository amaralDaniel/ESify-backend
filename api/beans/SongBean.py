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

    from esify import session
    from api.beans.AccountBean import get_user

    try:
        title = data.get('title')
        print "title:"+title
        artist = data.get('artist')
        print "artist:"+artist
        user = get_user(session["X-Auth-Token"])
        print user
        song = Song(title, artist, user)
        db.session.add(song)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False
