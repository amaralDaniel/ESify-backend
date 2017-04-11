import os

from markupsafe import Markup
import json

from flask import redirect, url_for, escape, request

from esify import app, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/songs'
ALLOWED_EXTENSIONS = set(['mp3','wav','aac'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/song',methods=['GET', 'POST'])
def upload_song():
    if request.method == 'POST' :
        if 'song_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        song_file = request.files['song_file']
        if song_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if song_file and allowed_file(song_file.filename):
            filename = secure_filename(song_file.filename)
            song_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=song_file>
         <input type=submit value=Upload>
    </form>
    '''
