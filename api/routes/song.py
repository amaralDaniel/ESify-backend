import os

from markupsafe import Markup
import json

from flask import redirect, url_for, escape, request, flash, send_from_directory, render_template


from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['mp3','wav','aac'])
# flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/song',methods=['GET', 'POST'])
# def upload_song():
#     if request.method == 'POST' :
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',filename=filename))
#         if file and not (allowed_file(file.filename)):
#             filename = secure_filename(file.filename)
#             flash('Incompatible media type')
#             return render_template('song.html')
#     return render_template('song.html')
#
#
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)
