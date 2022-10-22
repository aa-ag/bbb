import psycopg2
from config import user,password,host,port,database

# print(user,password,host,port,database)

connection = None

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )

        cursor = connection.cursor()

        print("PostgreSQL server information")

        cursor.execute("SELECT version();")

        record = cursor.fetchone()

        print("Connected to ", record)

    except (Exception, psycopg2.Error) as error:
        print(error)

    if connection:
        cursor.close()
        connection.close()
        print("Connection closed.")


if __name__ == "__main__":
    connect_to_db()