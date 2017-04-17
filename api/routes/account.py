import os
from markupsafe import Markup
import json
import logging

from flask import request
from flask_restplus import Resource
from api.beans.AccountBean import get_account, update_account, delete_account
from api.beans.AuthBean import verify_token
from api.restplus import api


ns = api.namespace('account', description='Operations related to account')

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
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403
        user = get_account(session["X-Auth-Token"])

        return user, 200

    @api.response(200, 'Updated account information')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def put(self):
        """
        Updates account information to the user
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403

        data = request.json

        if update_account(session["X-Auth-Token"], data):
            return None, 200
        else:
            return None, 400

    @api.response(200, 'Deleted account ')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden accesss')
    def delete(self):
        """
        Delete account from the service
        """
        from esify import session
        if not verify_token(session["X-Auth-Token"]):
            session.clear()
            return None, 403
        if delete_account(session["X-Auth-Token"]):
            return None, 200
        else:
            return None, 400



