import logging

from flask import request
from flask_restplus import Resource, fields

from api.beans.AuthBean import register, login, logout
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('authentication', description='Operations related to authentication')

node_put_parser = api.parser()

package = api.model(
        "Creadentials",
        {
                "username": fields.String(
                        description="acess username",
                        required=True,
                        default="Account username"
                ),
                "password": fields.String(
                        description="platform password",
                        required=True,
                        default="Account password"
                ),
                "email": fields.String(
                        description="platform email",
                        required=True,
                        default="Account email"
                )

        }
)
node_put_parser.add_argument(
    'credentials',
    type=package, required=True, help='Account access email',
    location='json')
@ns.route('/register')
class Register(Resource):

    @api.response(200, 'User registered')
    @api.response(400, 'Invalid Credentials')
    # TODO: serializers
    @api.doc(body=package)
    def post(self):
        """
        Enables users to register in the platform.
        """
        data = request.json

        register(data)
        return "User Successfully Registered", 200

@ns.route('/login')
class Login(Resource):

    @api.response(200, 'User successfully logged in')
    @api.response(400, 'Invalid Username/Password')
    @api.doc(body=package)
    def post(self):
        """
        Enables users to login in the platform.
        """
        data = request.json
        print data.get('email')
        print data.get('password')
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
