#### tinkering with models for now
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

### set up
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

### Mission
class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_country = db.Column(db.String(2), nullable=False)
    home_country_flag_url = db.Column(db.String(255), nullable=False)
    destination_city = db.Column(db.String(3), nullable=False)
    # team = this probably needs to be a different table
    destination_address = db.Column(db.Text(), nullable=False)
    destination_phone = db.Column(db.Numeric(), nullable=False)
    '''
    - flag
    - team
    - address
    - services
    - faqs
    - social channels
    - contact
    '''

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)