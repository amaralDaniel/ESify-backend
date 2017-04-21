import os
from markupsafe import Markup
import json
import logging

from flask import request
from flask_restplus import Resource, fields
from api.beans.AccountBean import get_account, update_account, delete_account
from api.beans.AuthBean import verify_token
from api.restplus import api


ns = api.namespace('account', description='Operations related to account')
node_put_parser = api.parser()

account_info = api.model(
        "Credentials",
        {
                "username": fields.String(
                        description="Username",
                        default="user"
                ),
                "password": fields.String(
                        description="User password",
                        default="pass"
                )
                ,
                "email": fields.String(
                        description="User email",
                        default="a@bmail.com"
                )
        }

)

node_put_parser.add_argument(
    'account_info',
    type=account_info, required=True, help='Account access info',
    location='json')

@ns.route('/')
class Settings(Resource):

    @api.response(200, 'Retrieved account information')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def get(self):
        """
        Retrieves account information to the user
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden accesss", 403
        else:
            return get_account(session['X-Auth-Token']),200



    @api.response(200, 'Updated account information')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    @api.doc(body=account_info)
    def put(self):
        """
        Updates account information to the user
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden accesss", 403
        data = request.json
        if update_account(session["X-Auth-Token"], data):
            return 'Updated account information', 200
        else:
            return 'Bad Request', 400



    @api.response(200, 'Deleted account')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def delete(self):
        """
        Delete account from the service
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden accesss", 403
        if delete_account(session["X-Auth-Token"]):
            return 'Deleted account', 200
        else:
            return 'Bad Request', 400
