import psycopg2 as psy
import csv
conn = psy.connect("host=localhost dbname=postgres user=postgres password=132428")
cur = conn.cursor()

with open('E:/project_DigitalSkola/Project3/data/dataset.csv','r') as f:
    next(f)

    cur.copy_from(f, 'sekolah_siswaipa', sep=',', columns={'kelas','name','phone','postalzip'})    
conn.commit()