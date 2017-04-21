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
        user = get_user(session["X-Auth-Token"])
    except Exception as e:
        print e
        return False


    try:
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        release_year = request.form['release_year']
        file = request.files['song']
    except Exception as e:
        print e
        return False
    try:
        song = Song(title, artist, album, release_year, "" ,user.username)
        db.session.add(song)
        db.session.commit()
    except Exception as e:
        print e
        return False

    try:
        if file and allowed_file(file.filename):
            Song.query.filter_by(path_to_file="").first_or_404()
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
            song_obj = {}
            song_obj['artist'] = obj.artist
            song_obj['title'] = obj.title
            song_obj['album'] = obj.album
            song_obj['release_year'] = obj.release_year
            data[obj.id] = song_obj
        data2 = json.loads(json.dumps(data))
        return data2
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
    from esify import session
    try:
        Song.query.filter_by(id=song_id).update(dict(uploader='admin'))
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def update_song_info(song_id, data):
    try:
        song = Song.query.filter_by(id=song_id).first_or_404()
        if(data.get('artist')!=None):
            song.artist = data.get('artist')
        if(data.get('title')!=None):
            song.title = data.get('title')
        if(data.get('release_year')!=None):
            song.release_year = data.get('release_year')
        if(data.get('album')!=None):
            song.album = data.get('album')
        db.session.add(song)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def search_song_by(data):
    try:

        if(data.get('artist')!=None and data.get('title')!=None):
            artist = data.get('artist')
            title = data.get('title')
            songs_list = Song.query.filter_by(artist=artist,title=title).all()
            data = {}
            data = {}
            for obj in songs_list:
                song_obj = {}
                song_obj['artist'] = obj.artist
                song_obj['title'] = obj.title
                song_obj['album'] = obj.album
                song_obj['release_year'] = obj.release_year
                data[obj.id] = song_obj
            data2 = json.loads(json.dumps(data))
            return data2
        elif(data.get('artist')!=None and data.get('title')==None):
            artist = data.get('artist')
            songs_list = Song.query.filter_by(artist=artist).all()
            data = {}
            data = {}
            for obj in songs_list:
                song_obj = {}
                song_obj['artist'] = obj.artist
                song_obj['title'] = obj.title
                song_obj['album'] = obj.album
                song_obj['release_year'] = obj.release_year
                data[obj.id] = song_obj
            data2 = json.loads(json.dumps(data))
            return data2
        elif(data.get('artist')==None and data.get('title')!=None):
            title = data.get('title')
            songs_list = Song.query.filter_by(title=title).all()
            data = {}
            data = {}
            for obj in songs_list:
                song_obj = {}
                song_obj['artist'] = obj.artist
                song_obj['title'] = obj.title
                song_obj['album'] = obj.album
                song_obj['release_year'] = obj.release_year
                data[obj.id] = song_obj
            data2 = json.loads(json.dumps(data))
            return data2
        else:
            return False
    except Exception as e:
        print e
        return False
