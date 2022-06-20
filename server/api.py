############------------ IMPORTS ------------############
### external imports
import json
from flask import jsonify, request
### internal imports
from configuration import *
from models import *
from collections import defaultdict

############------------ ROUTE(S) ------------############
@app.route('/calendar', methods=['GET'])
def calendar():
    '''
     query the DB for all missions, 
     format the result into a payload with home_countries 
     & destination_cities
    '''
    return "Calendar"



@app.route('/admin', methods=['GET', 'POST'])
def add_mission():
    '''
     handle POST request for /admin route,
     format the request, and add a new mission
     to the db
    '''
    if request.method == 'POST':
        data = request.get_json()
        new_mission = Mission(
            home_country=data["home_country"],
            destination_city=data["destination_city"],
        )
        db.session.add(new_mission)
        db.session.commit()
        return {"message": "new mission added!"}


@app.route('/directory', methods=['GET', 'POST'])
def directory():
    '''
     Use user input from the frontend, to query the db
     for a given mission;  if a match is found, returns 
     db data for destination_cities
    '''
    if request.method == 'POST':
        data = request.get_json()
        missions_query = Mission.query.filter(
            Mission.home_country == data["home_country"],
            Mission.destination_city == data["destination_city"]
        ).all()
        
        all_matches = [
            mission.destination_city for mission in missions_query
        ]
            
        return {
            "count": f"consulates found for {data['home_country']}: {len(all_matches)}",
            "missions": all_matches
        }


@app.route('/browse', methods=['GET'])
def browse():
    if request.method == 'GET':
        query = Mission.query.all()

        missions = dict()
        
        for mission in query:
            missions[mission.home_country] = 0

        for mission in query:
            missions[mission.home_country] += 1

        return {"missions": missions}


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()