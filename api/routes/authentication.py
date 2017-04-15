import os
from markupsafe import Markup
import json
import logging

from flask import redirect, url_for, escape, request
from flask_restplus import Resource
from api.beans.AuthBean import register, login
from api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('authentication', description='Operations related to authentication')



@ns.route('/register')
class Register(Resource):

    @api.response(200, 'Test')
    def get(self):
        """
        Get just for testing.
        """

    @api.response(200, 'User registered')
    # TODO: serializers
    def post(self):
        """
        Enables users to register in the platform.
        """
        data = request.json

        register(data)
        return None, 200

# @ns.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         username = request.form['username']
#
#         from beans import AuthBean
#
#         bean = AuthBean()
#
#         if bean.login( email , password):
#             return 'LOGGED'
#         else:
#             return 'NOT'
#     else:
#         return '''
#             <form method="post">
#                 <p><input type=text name=email>
#                 <p><input type=password name=password>
#                 <p><input type=submit value=Login>
#             </form>
#         '''
#
#

# @ns.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))
