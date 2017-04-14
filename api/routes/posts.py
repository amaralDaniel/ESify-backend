import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('routes/posts', description='Operations related to blog posts')


@ns.route('/')
class PostsCollection(Resource):

    def get():
        return "get"
