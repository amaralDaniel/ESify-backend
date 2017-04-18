import logging

from flask import request
from flask_restplus import Resource

from api.beans.AuthBean import register, login, logout
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('song', description='Operations related to songs')

@ns.route('/song')
class Song(Resource):
    @api.response(200, 'Song Uploaded')

    def post(self):
        """
        Enables users to upload songs to the platform.
        """
        data = request.json

        register(data)
        return None, 200
