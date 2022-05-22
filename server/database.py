############------------ IMPORTS ------------############
import psycopg2
from settings import db_url

############------------ QUERIES ------------############
CREATE_MISSION_TABLE = '''
CREATE TABLE IF NOT EXISTS mission (
    home_country TEXT,
    destination_city TEXT
);
'''

############------------ GLOBAL VARIABLE(S) ------------############
connection = psycopg2.connect(db_url)
cursor = connection.cursor()
cursor.execute(CREATE_MISSION_TABLE)
cursor.execute("SELECT version();")
version = cursor.fetchone()
print(version)
connection.close()