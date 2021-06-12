#!/usr/bin/python

import os
import psycopg2

USER = os.getenv("USER", "postgres")
PASSWORD = os.getenv("PASSWORD", "16oLdhku2P")
HOST = os.getenv("HOST", "aqi-postgresql-headless.postgresql")
PORT = os.getenv("PORT", "5432")
DATABASE = os.getenv("DATABASE", "postgres")

conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,port=PORT)
print("Opened database successfully")

cur = conn.cursor()

cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")

conn.close()