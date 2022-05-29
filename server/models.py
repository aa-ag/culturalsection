############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############


############------------ MODEL(S) ------------############



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