############------------ IMPORTS ------------############
from flask import Flask, jsonify
from flask_cors import CORS


############------------ GLOBAL VARIABLE(S) ------------###########
### app configuration
DEBUG = True

### app instantiation
app = Flask(__name__)
app.config.from_object(__name__)

############------------ ROUTE(S) ------------############
@app.route('/', methods=['GET'])
def hello():
    return jsonify('World')


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()