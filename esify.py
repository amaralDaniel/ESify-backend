from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import settings
# from rest_api_demo.api.blog.endpoints.posts import ns as blog_posts_namespace
# from rest_api_demo.api.blog.endpoints.categories import ns as blog_categories_namespace
from api.restplus import api
from models import db

app = Flask(__name__)

SONGS_FOLDER = '/songs'

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
    # api.add_namespace(blog_posts_namespace)
    # api.add_namespace(blog_categories_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

def main():
    initialize_app(app)
    print ">>>>> Starting development server at http://{}/api/ <<<<<".format(app.config['SERVER_NAME'])

    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()
