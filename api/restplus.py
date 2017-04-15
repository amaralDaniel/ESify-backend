import logging
import traceback

from flask_restplus import Api
import settings
from sqlalchemy.orm.exc import NoResultFound



api = Api(version='1.0', title='ESify-backend',
          description='Backend for Esify, a platform to manage your music')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404
