############------------ IMPORTS ------------############
from flask import Flask, jsonify
from flask_cors import CORS

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