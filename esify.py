from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/esify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


if __name__ == '__main__':
    try:
        from models import *
        db.create_all()
        db.session.commit()
    except Exception as e:
        print e
    app.run()
