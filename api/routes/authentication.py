import os
from markupsafe import Markup
import json
import logging

from flask import redirect, url_for, escape, request
from flask_restplus import Resource
from api.beans import AuthBean, UserPlaylistBean, AccountBean
from api.restplus import api
from models import User

log = logging.getLogger(__name__)

ns = api.namespace('api/authentication', description='Operations related to authentication')



@ns.route('/')
class Authentication(Resource):
    def get():
        print "jelly-hoe"
        pass

# @ns.route('/register', methods=['POST'])
# class Register(Resource):
#
#
#     def get(self):
#         """
#         Enables users to register in the platform.
#         """
#         return None, 200
#     # email = request.form['email']
#     # password = request.form['password']
#     # username = request.form['username']
#     # from beans import AuthBean
#     # bean = AuthBean()
#     # if bean.register( email , password, username):
#     #     return 'REGISTERED'
#     # return 'NOT REGISTERED'



#
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
