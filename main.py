import psycopg2


conn = psycopg2.connect(
    dbname="ReservationByAPI",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)


with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            date DATE NOT NULL,
            time TIME NOT NULL,
            guests INTEGER NOT NULL
        );
    """)
    conn.commit()
