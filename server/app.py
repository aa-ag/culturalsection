############------------ IMPORTS ------------############
from venv import create
from flask import Flask, jsonify, request
from flask_cors import CORS
from settings import db_url
from flask_migrate import Migrate
from models import db, Mission
import psycopg2
from sqlalchemy import create_engine

############------------ GLOBAL VARIABLE(S) ------------###########
### app configuration
DEBUG = True

### app instantiation
app = Flask(__name__)
app.config.from_object(__name__)

### enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

### db configuration
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = create_engine(db_url)

############------------ ROUTE(S) ------------############
@app.route('/calendar', methods=['GET'])
def calendar():
    response_object = {'status': 'success'}
    if request.method == 'GET':
        query = db.execute('SELECT * FROM mission')
        missions = list()
        for mission in query:
            missions.append({f'{mission.home_country}': f'{mission.destination_city}'})
        response_object['missions'] = missions
    return jsonify(response_object)


@app.route('/admin', methods=['GET', 'POST'])
def add_mission():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        connection = psycopg2.connect(db_url)
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO mission (home_country, destination_city) VALUES (%s, %s)',
                (post_data["homecountry"],post_data["destinationcity"])
            )
        connection.close()

        response_object['message'] = 'Mission added!'
    return jsonify(response_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()