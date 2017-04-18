import logging

from flask import json
from flask import request, redirect
from flask import jsonify
from flask_restplus import Resource

from api.beans.AuthBean import verify_token
from api.beans.PlaylistBean import create_playlist, verify_owner, get_playlist, update_playlist, delete_playlist, get_all_playlists
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('playlist', description='Operations related to playlist')

@ns.route('/')
class PlaylistCollection(Resource):

    #TODO serielizer
    @api.response(200, 'Retrieved playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def post(self):
        """
        Creates a new playlist
        """
        data = request.json

        if create_playlist(data):
            return None, 200
        else:
            return None, 403


    @api.response(200, 'Retrieved all playlists')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def post(self):
        """
        Gets all playlists
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

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
        if delete_playlist(id):
            return None, 200
        else:
            return None, 400



