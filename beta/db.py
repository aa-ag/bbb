import psycopg2
from config import user,password,host,port,database

# print(user,password,host,port,database)

connection = None

def connect_to_db():
    connection = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database,
    )

    cursor = connection.cursor()
    return cursor

def test_connect(cur):
    try:
        print("PostgreSQL server information")

        cur.execute("SELECT version();")

        record = cur.fetchone()

        print("Connected to ", record)
        return record

    except (Exception, psycopg2.Error) as error:
        print(error)


# def close_connection():
#     if connection:
#         cursor.close()
#         connection.close()
#         print("Connection closed.")


if __name__ == "__main__":
    cur = connect_to_db()
    test_connect(cur)
