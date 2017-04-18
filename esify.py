from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import session
import settings
from api.routes.authentication import ns as authentication_ns
from api.routes.account import ns as account_ns
from api.routes.playlist import ns as playlist_ns
from api.routes.song import ns as song_ns

from api.restplus import api
from models import db

app = Flask(__name__)

SONGS_FOLDER = '/uploads'

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(flask_app)
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

    flask_app.config['SONGS_UPLOADED'] = SONGS_FOLDER
    # set the secret key.  keep this really secret:
    flask_app.secret_key = "\xe4IX\x1a\xf4\x9b\x80'K\xb1\xa1L\xba\xcd\xe5\xb0Ts\xfal\xe3NB\xa1"

def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(authentication_ns)
    api.add_namespace(account_ns)
    api.add_namespace(playlist_ns)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()

def main():
    initialize_app(app)
    print ">>>>> Starting development server at http://{}/api/ <<<<<".format(app.config['SERVER_NAME'])

    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()
