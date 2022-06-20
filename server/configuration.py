############------------ IMPORTS ------------############
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import db_url
from flask_cors import CORS
from flask_migrate import Migrate
from pprint import pprint

### app configuration
DEBUG = True

### app instantiation
app = Flask(__name__)
app.config.from_object(__name__)

### db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

### enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})