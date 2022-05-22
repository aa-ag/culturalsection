############------------ IMPORTS ------------############
from flask_sqlalchemy import SQLAlchemy


############------------ GLOBAL VARIABLE(S) ------------############
db = SQLAlchemy()


############------------ MODEL(S) ------------############
class Mission(db.Model):
    '''
     main unit in platform: mission-centric. 
     Countries send missions to other countries, 
     and those missions have both embassies in destination countries,
     and consulates in other cities in destination countriesß
    '''
    __tablename__ = 'mission'
    
    id = db.Column(db.Integer, primary_key=True)
    home_country = db.Column(db.Text(), nullable=False)
    # home_country_flag_url = db.Column(db.String(255), nullable=False)
    destination_city = db.Column(db.Text(), nullable=False)
    # team = db.Column(db.JSON(), nullable=True)
    # destination_address = db.Column(db.Text(), nullable=False)
    # destination_phone = db.Column(db.Numeric(), nullable=False)
    # team = db.Column(db.JSON(), nullable=False)
    # social_links = db.Column(db.JSON(), nullable=False)

    # def __init__(self):
    #     pass

    # def __repr__(self):
    #     pass

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text(), nullable=False)
    first_name = db.Column(db.Text(), nullable=False)
    last_name = db.Column(db.Text(), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    when = db.Column(db.DateTime(), nullable=False)
    where = db.Column(db.Text(), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, nullable=False)

class FQA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mission = db.Column(db.Integer, nullable=False)

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    db.create_all()
    db_app.run(debug=True)