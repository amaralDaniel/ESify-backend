import os

from markupsafe import Markup
import json

from flask import redirect, url_for, escape, request
from esify import app, session

@app.route('/account', methods=['POST'])
def user_account():
    from beans import AuthBean
    bean = AuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return redirect(url_for('index'))
    return "X AUTH TOKEN NICE"

@app.route('/dashboard', methods=['POST'])
def user_dashboard():
    from beans import AuthBean
    bean = AuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return redirect(url_for('index'))
    from beans import UserPlaylistBean
    bean = UserPlaylistBean(session["X-Auth-Token"])
    playlists = bean.get_user_playlists()
    return "USER PLAYLISTS "

@app.route('/delete/account', methods=['POST'])
def delete_account():
    from beans import AuthBean
    bean = AuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return redirect(url_for('index'))
    from beans import AccountBean
    bean = AccountBean(session["X-Auth-Token"])
    if bean.delete_account():
        return redirect(url_for('logout'))
    else:
        return "SOMETHING WENT WRONG"
