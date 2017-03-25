from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)
from routes import *

SONGS_FOLDER = '/songs'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/esify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

app.config['SONGS_UPLOADED'] = SONGS_FOLDER
# set the secret key.  keep this really secret:
app.secret_key = "\xe4IX\x1a\xf4\x9b\x80'K\xb1\xa1L\xba\xcd\xe5\xb0Ts\xfal\xe3NB\xa1"

if __name__ == '__main__':
    try:
        from models import *
        db.create_all()
        db.session.commit()
    except Exception as e:
        print e
    app.run()
