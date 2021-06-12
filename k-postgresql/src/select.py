#!/usr/bin/python

import os
import psycopg2

USER = os.getenv("USER", "postgres")
PASSWORD = os.getenv("PASSWORD", "16oLdhku2P")
HOST = os.getenv("HOST", "aqi-postgresql.postgresql")
PORT = os.getenv("PORT", "5432")
DATABASE = os.getenv("DATABASE", "postgres")

conn = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD,port=PORT)
print("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

conn.close()