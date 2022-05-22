############------------ IMPORTS ------------############
from flask import Flask, jsonify
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

############------------ ROUTE(S) ------------############
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'success',
        'example_cities': '',
    })


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()