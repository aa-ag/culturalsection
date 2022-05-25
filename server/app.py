############------------ IMPORTS ------------############
from flask import Flask, jsonify, request
from flask_cors import CORS
from settings import db_url
from flask_migrate import Migrate
from models import db, Mission

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
@app.route('/', methods=['GET'])
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
    # print(request)
    # return jsonify({
    #     'status': 'success'
    # })
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        # mission = Mission(request.home_country,request.destination_city)
        # db.session.add(mission)
        # db.session.commit()
        # response_object['message'] = 'Mission added!'
    return jsonify(response_object)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()