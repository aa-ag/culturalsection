############------------ IMPORTS ------------############
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from settings import db_url
from flask_cors import CORS


############------------ GLOBAL VARIABLE(S) ------------###########
### app configuration
DEBUG = True

### app instantiation
app = Flask(__name__)
app.config.from_object(__name__)

### db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

### enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})



############------------ ROUTE(S) ------------############
@app.route('/calendar', methods=['GET'])
def calendar():
    pass


@app.route('/admin', methods=['GET', 'POST'])
def add_mission():
    pass


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()