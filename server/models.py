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
    country = db.Column(db.String(80), nullable=False)