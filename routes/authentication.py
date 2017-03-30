import os

from markupsafe import Markup
import json

from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/')
def index():
    def index(): pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        from beans import AuthBean
        bean = AuthBean()
        if bean.login( email , password):
            return 'LOGGED'
        else:
            return 'NOT'
    else:
        return '''
            <form method="post">
                <p><input type=text name=email>
                <p><input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        '''

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
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
