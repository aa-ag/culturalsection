############------------ IMPORTS ------------############
import psycopg2
from settings import db_url

############------------ QUERIES ------------############
# query to create the mission table
CREATE_MISSION_TABLE = '''
CREATE TABLE IF NOT EXISTS mission (
    home_country TEXT,
    destination_city TEXT
);
'''
# query to insert one mission
INSERT_MISSION = """
INSERT INTO mission (home_country, destination_city) VALUES ('USA', 'Zug');
"""

############------------ GLOBAL VARIABLE(S) ------------############
connection = psycopg2.connect(db_url)


############------------ FUNCTION(S) ------------############
def test_connection():
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(version)
    connection.close()

def create_tables():
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    cursor.execute(CREATE_MISSION_TABLE)
    connection.close()


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_connection()
    create_tables()