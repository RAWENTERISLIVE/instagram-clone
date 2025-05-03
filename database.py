import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        conn = sqlite3.connect('instagram.db')
        return conn
    except Error as e:
        print(e)
        return None

def create_tables():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            
            # Create users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    fullname TEXT NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            print("Database tables created successfully")
        except Error as e:
            print(e)
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    create_tables()
