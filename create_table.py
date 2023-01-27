import psycopg2 as psy

conn = psy.connect("host=localhost dbname=postgres user=postgres password=132428")
cur = conn.cursor()
try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sekolah_siswaIpa(
            id serial PRIMARY KEY,
            kelas text,
            name text,
            phone text,
            postalZip text
            )
    """ )
    print("Sukses membuat tabel")
except:
    print("Error")

conn.commit()