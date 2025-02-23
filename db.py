import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-split-securin.j.aivencloud.com",
  password="AVNS_11cCcE1gngh_ISfOnvf",
  read_timeout=timeout,
  port=20262,
  user="avnadmin",
  write_timeout=timeout,
)
  
try:
  cursor = connection.cursor()
  cursor.execute("show tables")
  print(cursor.fetchall())
finally:
  connection.close()