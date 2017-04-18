import os
from os.path import join, dirname, realpath
from models import db
from models.Song import Song
from flask import json
from flask import redirect, url_for, escape, request
from werkzeug.utils import secure_filename



ALLOWED_EXTENSIONS = set(['mp3','wav','aac'])
#tem de ser criada se nao existir
UPLOAD_FOLDER = './uploads/'

def __init__(self):
    pass



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def upload(request):

    from esify import session
    from api.beans.AccountBean import get_user


    try:
        title = request.form['title']
        artist = request.form['artist']
        user = get_user(session["X-Auth-Token"])
        file = request.files['song']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        song = Song(title, artist, user)
        db.session.add(song)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False
