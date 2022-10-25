import psycopg2
from config import user,password,host,port,database

connection = None

def connect_to_db():
    connection = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    
    return connection
