import logging
from flask import json
from flask import request, redirect
from flask import jsonify
from flask_restplus import Resource

from api.beans.AuthBean import register, login, logout
from api.beans.SongBean import upload, get_all_songs
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
