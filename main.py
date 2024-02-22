import psycopg2


def create_db():
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Clients(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(60) UNIQUE
        last_name VARCHAR(60) UNIQUE
        email TEXT UNIQUE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Phones(
        id SERIAL PRIMARY KEY,
        client_id INTEGER,
        phone_number TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES Clients(id)
    );
    """)

    conn.commit()
    conn.close()

def add_client(first_name, last_name, email):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""INSERT INTO Clients (first_name, last_name, email)
                     VALUES (%s, %s, %s)""", (first_name, last_name, email))

    conn.commit()
    conn.close()

def add_phone(client_id, phone):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""INSERT INTO Clients (client_id, phone)
                     VALUES (%s, %s, %s)""", (client_id, phone))

    conn.commit()
    conn.close()

def change_client(client_id, first_name=None, last_name=None, email=None):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    if first_name:
        cur.execute("""UPDATE Clients SET first_name = %s WHERE id = %s""", (first_name, client_id))
    if last_name:
        cur.execute("""UPDATE Clients SET last_name = %s WHERE id = %s""", (last_name, client_id))
    if email:
        cur.execute("""UPDATE Clients SET email = %s WHERE id = %s""", (email, client_id))

    conn.commit()
    conn.close()

def delete_phone(client_id, phone):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""DELETE FROM Phones WHERE id=%s""", (phone, client_id))

    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""DELETE FROM Clients WHERE id=%s""", (client_id,))

    conn.commit()
    conn.close()

def find_client(first_name=None, last_name=None, email=None, phone=None):
    conn = psycopg2.connect(database="python_db", user="postgres", password="postgres")
    cur = conn.cursor()

    cur.execute("""SELECT id FROM Clients WHERE first_name LIKE %s 
             OR last_name LIKE %s OR email = %s OR id IN (SELECT client_id FROM Phones WHERE phone_number = %s);""", (first_name, last_name, email, phone))

    conn.close()
    return cur.fetchone()



