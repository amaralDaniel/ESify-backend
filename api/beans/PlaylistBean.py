# TODO get_all, get_by_id, delete, update, add_music, remove_music
from flask import json

from models import db
from models.Playlist import Playlist

def create_playlist(data):


    from esify import session
    from AccountBean import get_user

    try:

        user = get_user(session["X-Auth-Token"])

        title = data.get('title')
        description = data.get('description')
        owner = user

        playlist = Playlist(title, description, owner, {})
        db.session.add(playlist)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False


def verify_owner(playlist_id, token):
    from api.beans.AccountBean import get_user


    user = get_user(token)
    playlist = Playlist.query.filter_by(id=playlist_id).first_or_404()
    owner = playlist.owner
    if user.id == owner:
        return True
    else:
        return False


def get_playlist(playlist_id):

    try:
        playlist = Playlist.query.filter_by(id=playlist_id).first_or_404()

        data = {}
        data['title'] = playlist.title
        data['description'] = playlist.description

        playlist_data = json.dumps(data)
        return playlist_data
    except Exception as e:
        print e


def update_playlist(playlist_id, data):

    try:
        playlist = Playlist.query.filter_by(id=playlist_id).first_or_404()
        playlist.title = data.get('title')
        playlist.description = data.get('description')

        db.session.add(playlist)
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

def delete_playlist(playlist_id):
    try:
        playlist = Playlist.query.filter(Playlist.id == playlist_id).first_or_404()
        db.session.delete(playlist)
        #TODO check cascading delete
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False

