import psycopg2 as psy
import csv

conn = psy.connect("host=localhost dbname=postgres user=postgres password=132428")

#menggunakan cursor
cur = conn.cursor()
cur.execute('Select * from public.sekolah_siswaipa')

#menampilkan hasil
one = cur.fetchone()
all = cur.fetchall()
print(one)