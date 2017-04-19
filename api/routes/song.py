import logging
from flask import json
from flask import request, redirect
from flask import jsonify
from flask_restplus import Resource

from api.beans.AuthBean import register, login, logout, verify_token
from api.beans.SongBean import upload, get_all_songs, verify_owner, delete_song
from api.restplus import api
from models.Song import Song


log = logging.getLogger(__name__)

ns = api.namespace('song', description='Operations related to songs')

@ns.route('/upload')
class Song(Resource):

    @api.response(200, 'Song Uploaded')
    def post(self):
        """
        Enables users to upload songs to the platform.
        """
        upload(request)
        return None, 200

@ns.route('/')
class Songs(Resource):
    @api.response(200, 'Songs retrieved')
    def get(self):
        """
        Retrieves all songs uploaded
        """
        list_songs = get_all_songs()
        if list_songs != {}:
            return list_songs, 200
        else:
            return "No songs found", 200


@ns.route('/<int:id>')
class ManageSongs(Resource):
    @api.response(200, 'Deleted playlist ')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def delete(self, id):
        """
        Delete uploaded songs
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403
        if not verify_owner(id, session["X-Auth-Token"]):
            return "you're not allowed", 403
        if delete_song(id):
            return None, 200
        else:
            return None, 400
