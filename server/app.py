############------------ IMPORTS ------------############
from operator import methodcaller
from flask import Flask, jsonify


############------------ GLOBAL VARIABLE(S) ------------###########
### app configuration
DEBUG = True

### app instantiation
app = Flask(__name__)
app.config.from_object(__name__)

############------------ ROUTE(S) ------------############



############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass