import os
import pymysql  
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        db=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        charset=os.getenv("DB_CHARSET"),
        connect_timeout=int(os.getenv("DB_TIMEOUT")),
        read_timeout=int(os.getenv("DB_TIMEOUT")),
        write_timeout=int(os.getenv("DB_TIMEOUT")),
        cursorclass=pymysql.cursors.DictCursor
    )



def show_tables():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables=cursor.fetchall()
        return tables
    finally:
        connection.close()

# print(show_tables())