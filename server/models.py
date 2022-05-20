#### tinkering with models for now
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

### set up
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

### Mission
class Mission(db.Model):
    '''
     main unit in platform: mission-centric. 
     Countries send missions to other countries, 
     and those missions have both embassies in destination countries,
     and consulates in other cities in destination countriesß
    '''
    id = db.Column(db.Integer, primary_key=True)
    home_country = db.Column(db.String(2), nullable=False)
    home_country_flag_url = db.Column(db.String(255), nullable=False)
    destination_city = db.Column(db.String(3), nullable=False)
    # team = this probably needs to be a different table
    destination_address = db.Column(db.Text(), nullable=False)
    destination_phone = db.Column(db.Numeric(), nullable=False)
    team = db.Column(db.Json(), nullable=False)
    
    '''
    - social channels / links
    '''

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, foreing_key=True, nullable=False)
    title = db.Column(db.Text(), nullable=False)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, foreing_key=True, nullable=False)
    title = db.Column(db.Text(), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, foreing_key=True, nullable=False)

class FQA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, foreing_key=True, nullable=False)