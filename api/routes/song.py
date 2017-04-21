import logging
from flask import json
from flask import request, redirect, session
from flask import jsonify
from flask_restplus import Resource, fields
from werkzeug.datastructures import FileStorage
from api.beans.AuthBean import register, login, logout, verify_token
from api.beans.SongBean import upload, get_all_songs, verify_owner, delete_song, update_song_info, search_song_by
from api.restplus import api
from models.Song import Song
from api.beans.AccountBean import get_user

log = logging.getLogger(__name__)

ns = api.namespace('song', description='Operations related to songs')
parser = api.parser()
parser.add_argument('title', type=str, help='Song title', location='form')
parser.add_argument('album', type=str, help='Album title', location='form')
parser.add_argument('artist', type=str, help='Song artist name', location='form')
parser.add_argument('release_year', type=int, help='Album title', location='form')
parser.add_argument('song', type=FileStorage, location='files')


node_put_parser = api.parser()
song_put_parser = api.parser()

song_info = api.model(
        "Song_info",
        {
                "title": fields.String(
                        description="Song title",
                        required=False,
                        default="song title"
                ),
                "artist": fields.String(
                        description="Song artist",
                        required=False,
                        default="song author"
                )
        }
)

song_info_update = api.model(
        "Song_info_update",
        {
                "title": fields.String(
                        description="Song title",
                        required=False,
                        default="song title"
                ),
                "artist": fields.String(
                        description="Song artist",
                        required=False,
                        default="song author"
                ),
                "album": fields.String(
                        description="Song album",
                        required=False,
                        default="song album"
                ),
                "release_year": fields.Integer(
                        description="Song year",
                        required=False,
                        default="song realease year"
                ),
        }
)


node_put_parser.add_argument(
    'song_info',
    type=song_info, required=True, help='Song info',
    location='json')

song_put_parser.add_argument(
    'song_info_upadate',
    type=song_info_update, required=True, help='Song info',
    location='json')
@ns.route('/upload')
class Song(Resource):

    @api.response(200, 'Song Uploaded')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden Access')
    @api.expect(parser)
    def post(self):
        """
        Enables users to upload songs to the platform.
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden access", 403
        if(upload(request)==True):
            return "Song uploaded",200
        else:
            return 'Bad Request', 400


@ns.route('/')
class Songs(Resource):
    @api.response(200, 'Songs retrieved')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden Access')
    def get(self):
        """
        Retrieves all songs uploaded
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden access", 403
        list_songs = get_all_songs()
        if list_songs != {}:
            return list_songs, 200
        else:
            return "No songs found", 200


@ns.route('/<int:id>')
class ManageSongs(Resource):

    @api.response(200, 'Deleted song ')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden access')
    def delete(self, id):
        """
        Delete uploaded songs
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden access", 403
        if not verify_owner(id, session["X-Auth-Token"]):
            return 'Forbidden Access', 403
        if delete_song(id):
            return 'Song deleted successfully', 200
        else:
            return 'Bad Request' , 400

    @api.response(200, 'Updated playlist')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden access')
    @api.doc(body=song_info_update)
    def put(self, id):
        """
        Updates song info by ID
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden access", 403

        if not verify_owner(id, session["X-Auth-Token"]):
            return "Forbidden access", 403

        data = request.json
        if(update_song_info(id,data)):
            return 'Playlist info updated sucessfully',200
        else:
            return 'Bad Request', 400

@ns.route('/search')
class SearchSongs(Resource):
    @api.response(200, 'Songs Retrieved')
    @api.response(400, 'Bad Request')
    @api.response(403, 'Forbidden access')
    @api.doc(body=song_info)
    def post(self):
        """
        Retrieves songs by search criteria
        """
        from esify import session
        if(session.has_key('logged_in') != True):
            return "Forbidden access", 403
            
        data = request.json
        if(search_song_by(data)):
            song_list = search_song_by(data)
            return songs_list,200
        else:
            return 'Bad Request', 400
