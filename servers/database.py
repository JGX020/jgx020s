__author__ = '...'
import psycopg2




def seldatabase(tablename):
    conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+tablename+" ;")
    rows = cur.fetchall()        # all rows in table
    print(rows)
    conn.commit()
    cur.close()
    conn.close()
