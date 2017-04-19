# TODO get_all, get_by_id, delete, update, add_music, remove_music
from flask import json
from flask import session

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
        # TODO check cascading delete
        db.session.commit()
        return True
    except Exception as e:
        print e
        return False


def get_all_playlists(token):
    try:
        from api.beans.AccountBean import get_user

        user = get_user(token)
        playlist_list = Playlist.query.filter_by(owner=user.id).all()

        data = {}
        for obj in playlist_list:
            data[obj.title] = obj.description

        return json.dumps(data)

    except Exception as e:
        print e
        return False


def add_song_to_playlist(p_id, s_id):

    if verify_owner(p_id,session["X-Auth-Token"]):
        try:
            from models.Playlist import Playlist
            from models.Song import Song

            playlist = Playlist.query.filter_by(id=p_id).first_or_404()
            song = Song.query.filter_by(id=s_id).first_or_404()

            playlist.playlist_songs.append(song)
            db.session.commit()
        except Exception as e:
            print e
            return False


def remove_song_from_playlist(p_id, s_id):

    if verify_owner(p_id, session["X-Auth-Token"]):
        try:
            from models.Playlist import Playlist
            from models.Song import Song


        except Exception as e:
            print e
            return False

def detail_songs(p_id):

    try:
        from models.Playlist import Playlist

        playlist = Playlist.query.filter_by(id=p_id).first_or_404()

        data = {}
        for obj in playlist.playlist_songs:
            data[obj.title] = obj.artist

        return json.dumps(data)
    except Exception as e:
        print e
        return False
