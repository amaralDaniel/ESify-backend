import logging
from flask import json
from flask import request, redirect
from flask import jsonify
from flask_restplus import Resource

from api.beans.AuthBean import register, login, logout
from api.beans.SongBean import upload
from api.restplus import api


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
