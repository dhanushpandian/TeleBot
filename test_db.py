import pymysql
import os
from dotenv import load_dotenv
timeout = 10
load_dotenv()
connection = pymysql.connect(
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
  
try:
  cursor = connection.cursor()
  # f=open("sql.txt","r")
  # sql=f.read()
  # print(sql)
  # a=sql.split(";")
  # for i in range(len(a)-1):
  #   print(a[i])
  #   cursor.execute(a[i])
  cursor.execute("select * from Customers;")
  print(cursor.fetchall())
finally:
  connection.close()