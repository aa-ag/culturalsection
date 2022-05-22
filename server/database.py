############------------ IMPORTS ------------############
import psycopg2
from settings import db_url

############------------ GLOBAL VARIABLE(S) ------------############
connection = psycopg2.connect(db_url)

cursor = connection.cursor(db_url)

############------------ FUNCTION(S) ------------############
def create_tables():
    pass


############------------ QUERIES ------------############
