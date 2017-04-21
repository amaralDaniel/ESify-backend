import logging

from flask import json
from flask import request, redirect
from flask import jsonify
from flask_restplus import Resource,  fields
from werkzeug.datastructures import FileStorage
from api.beans.AuthBean import verify_token
from api.beans.PlaylistBean import create_playlist, verify_owner, get_playlist, update_playlist, delete_playlist, get_all_playlists, add_song_to_playlist, remove_song_from_playlist, detail_songs
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('playlist', description='Operations related to playlist')
node_put_parser = api.parser()

playlist_info = api.model(
        "Creadentials",
        {
                "title": fields.String(
                        description="Playlist title",
                        required=True,
                        default="Le playlist"
                ),
                "description": fields.String(
                        description="Playlist description",
                        required=True,
                        default="gym beats"
                )
        }
)

node_put_parser.add_argument(
    'playlist_info',
    type=playlist_info, required=True, help='Account access email',
    location='json')
@ns.route('/')
@ns.route('/register')
class PlaylistCollection(Resource):

    #TODO serielizer
    @api.response(200, 'Playlist Created')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    @api.doc(body=playlist_info)
    def post(self):
        """
        Creates a new playlist
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden accesss", 403
        data = request.json
        if (create_playlist(data)==True):
            return 'Playlist Created', 200
        else:
            return 'Bad Request', 400


    @api.response(200, 'Retrieved all playlists')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def get(self):
        """
        Gets all playlists
        """
        from esify import session

        if(session.has_key('logged_in') != True):
            return "Forbidden accesss", 403

        list_playlists = get_all_playlists(session["X-Auth-Token"])
        if list_playlists != {}:
            return list_playlists, 200
        else:
            return "No playlists found", 200


@ns.route('/<int:id>')
class Playlist(Resource):

    @api.response(200, 'Retrieved playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def get(self, id):
        """
        Retrieves a certain playlist by ID
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        if not verify_owner(id, session["X-Auth-Token"]):
            return "you're not allowed", 403
        playlist = get_playlist(id)
        return playlist, 200

    @api.response(200, 'Updated playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def put(self, id):
        """
        Updates a certain playlist by ID
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        if not verify_owner(id, session["X-Auth-Token"]):
            return "you're not allowed", 403

        data = request.json

        update_playlist(id, data)
        return None, 200

    @api.response(200, 'Deleted playlist ')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def delete(self, id):
        """
        Delete account from the service
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403
        if not verify_owner(id, session["X-Auth-Token"]):
            return "you're not allowed", 403
        if delete_playlist(id):
            return None, 200
        else:
            return None, 400


@ns.route('/<int:p_id>/<int:s_id>')
class PlaylistSong(Resource):

    @api.response(200, 'Add song to playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def post(self,p_id,s_id):
        """
        Add song to playlist
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        if add_song_to_playlist(p_id, s_id):
            return None, 200
        else:
            return None, 403


    @api.response(200, 'Remove song from playlist ')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def delete(self, p_id, s_id):
        """
        Delete account from the service
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        if remove_song_from_playlist(p_id, s_id):
            return None, 200
        else:
            return None, 403

@ns.route('/<int:id>/songs')
class PlaylistDetails(Resource):

    @api.response(200, 'Retrieved songs of playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden access')
    def get(self,id):
        """
        Details songs of a playlist
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        song_list = detail_songs(id)
        if song_list != {}:
            return song_list, 200
        else:
            return "No songs in playlist were found", 200
