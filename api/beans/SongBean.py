import os
from os.path import join, dirname, realpath
from models import db
from models.Song import Song
from flask import json
from flask import redirect, url_for, escape, request, session
from werkzeug.utils import secure_filename



ALLOWED_EXTENSIONS = set(['mp3','wav','aac'])
#tem de ser criada se nao existir
UPLOAD_FOLDER = './uploads/'

def __init__(self):
    pass



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def upload(request):

    from esify import session
    from api.beans.AccountBean import get_user
    try:
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        release_year = request.form['release_year']
        user = get_user(session["X-Auth-Token"])
        file = request.files['song']
        song = Song(title, artist, album, release_year, "" ,user.username)
        db.session.add(song)
        db.session.commit()
        song = Song.query.filter_by(path_to_file="").first_or_404()
        if file and allowed_file(file.filename):
            new_filename =str(song.id)+'.'+get_file_extension(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, new_filename))
            path_to_file = os.path.join(UPLOAD_FOLDER, new_filename)
        Song.query.filter_by(path_to_file="").update(dict(path_to_file=path_to_file))
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def get_all_songs():
    try:
        songs_list = Song.query.all()

        data = {}
        for obj in songs_list:
            data["title_song_id:"+str(obj.id)] = obj.title
            data["artist_song_id:"+str(obj.id)] = obj.artist
        return  json.dumps(data)
    except Exception as e:
        print e
        return False


def verify_owner(song_id, token):
    from api.beans.AccountBean import get_user
    user = get_user(token)
    song = Song.query.filter_by(id=song_id).first_or_404()
    owner = song.uploader
    if user.username == owner:
        return True
    else:
        return False

def delete_song(song_id):
    try:
        song = Song.query.all()

        for s in song:
            if s.id == song_id:
                db.session.delete(s)
                db.session.commit()
            return True
    except Exception as e:
        print e
        return False

def update_song_info(song_id, data):
    try:
        song = Song.query.filter_by(id=song_id).first_or_404()
        song.title = data.get('title')
        song.artist= data.get('artist')
        db.session.add(song)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def search_song_by(data):
    try:
        artist = data.get('artist')
        if(artist != ''):
            songs_list = Song.query.filter_by(artist=artist).all()
            data = {}
            for obj in songs_list:
                data["title_song_id:"+str(obj.id)] = obj.title
                data["artist_song_id:"+str(obj.id)] = obj.artist
            return  json.dumps(data)
    except Exception as e:
        print e
        return False
