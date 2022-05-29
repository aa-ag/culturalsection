############------------ IMPORTS ------------############
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from settings import db_url
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSON

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
migrate = Migrate(app, db)

### enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


############------------ MODEL(S) ------------###########
class Mission(db.Model):
    '''
     main unit in platform: mission-centric. 
     Countries send missions to other countries, 
     and those missions have both embassies in destination countries,
     and consulates in other cities in destination countries
    '''
    __tablename__ = 'mission'
    
    id = db.Column(db.Integer, primary_key=True)
    home_country = db.Column(db.Text(), nullable=False)
    destination_city = db.Column(db.Text(), nullable=False)
    # home_country_flag_url = db.Column(db.String(255), nullable=False)
    # team = db.Column(db.JSON(), nullable=True)
    # destination_address = db.Column(db.Text(), nullable=False)
    # destination_phone = db.Column(db.Numeric(), nullable=False)
    # team = db.Column(db.JSON(), nullable=False)
    # social_links = db.Column(db.JSON(), nullable=False)

    def __repr__(self):
        return f"Mission from {self.home_country} to {self.destination_city}."


############------------ ROUTE(S) ------------############
@app.route('/calendar', methods=['GET'])
def calendar():
    pass


@app.route('/admin', methods=['GET', 'POST'])
def add_mission():
    if request.method == 'POST':
        data = request.get_json()
        new_mission = Mission(
            home_country=data["homecountry"],
            destination_city=data["destinationcity"],
        )
        db.session.add(new_mission)
        db.session.commit()
        return {"message": "new mission added!"}


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()