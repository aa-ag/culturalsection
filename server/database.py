############------------ IMPORTS ------------############
import psycopg2
from sqlalchemy import insert
from settings import db_url

############------------ QUERIES ------------############
# query to create the mission table
CREATE_MISSION_TABLE = '''
CREATE TABLE IF NOT EXISTS mission (
    id BIGSERIAL PRIMARY KEY,
    home_country TEXT,
    destination_city TEXT
);
'''
# query to insert one mission
INSERT_MISSION = '''
INSERT INTO mission (id, home_country, destination_city) VALUES (1, 'USA', 'Zug');
'''

# query to fetch all missions from the db
QUERY_MISSIONS = '''
SELECT * FROM mission;
'''

############------------ GLOBAL VARIABLE(S) ------------############
connection = psycopg2.connect(db_url)


############------------ FUNCTION(S) ------------############
def test_connection():
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(version)

def create_tables():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_MISSION_TABLE)
    

def insert_test_mission():
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_MISSION)

def query_mission():
    with connection:
        cursor = connection.cursor()
        cursor.execute(QUERY_MISSIONS)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_connection()
    create_tables()
    insert_test_mission()
    query_mission()
    connection.close()