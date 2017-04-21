import logging

from flask import request
from flask_restplus import Resource

from api.beans.AuthBean import register, login, logout
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('authentication', description='Operations related to authentication')


@ns.route('/register')
class Register(Resource):

    @api.response(200, 'User registered')
    # TODO: serializers
    def post(self):
        """
        Enables users to register in the platform.
        """
        data = request.json

        register(data)
        return None, 200

@ns.route('/login')
class Login(Resource):

    @api.response(200, 'User successfully logged in')
    @api.response(400, 'Invalid Username/Password')
    def post(self):
        """
        Enables users to login in the platform.
        """
        data = request.json
        if(login(data)):
            return "User successfully logged in", 200
        else:
            return "Invalid Username/Password", 400


@ns.route('/logout')
class Logout(Resource):

    @api.response(200,'User successfully logged out')
    @api.response(400,'Error logging out')
    def get(self):
        """
        Enables users to logout from the platform.
        """
        if(logout()):
            return "User successfully logged out", 200
        else:
            return "Error logging out", 400
