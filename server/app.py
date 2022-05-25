############------------ IMPORTS ------------############
from flask import Flask, jsonify, request
from flask_cors import CORS
from settings import db_url
from flask_migrate import Migrate
from models import db, Mission
import psycopg2

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
 
db.init_app(app)
migrate = Migrate(app, db)

############------------ ROUTE(S) ------------############
@app.route('/calendar', methods=['GET'])
def home():
    q = Mission.query.all() 

    msg = ''
    for i in q:
        msg += f"Diplomatic mission from {i.home_country} in {i.destination_city}"

    return jsonify({
        'status': 'success',
        'example_cities': f'{msg}',
    })


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

        response_object['message'] = 'Mission added!'
    return jsonify(response_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()