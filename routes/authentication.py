import os

from markupsafe import Markup
import json

from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'logging you in'
    else:
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']
    username = data['username']
    from beans import AuthBean
    bean = AuthBean()
    if bean.register( email , password, username):
        return 'REGISTERED'
    return 'NOT REGISTERED'



@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
