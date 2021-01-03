import sqlite3
from datetime import datetime

def create_database_tables():
    try:
        db = sqlite3.Connection('data.db')
        cursor = db.cursor()
        create_users_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, date timestamp)'
        cursor.execute(create_users_table)

        create_applications_table = 'CREATE TABLE IF NOT EXISTS apllications (id INTEGER PRIMARY KEY, user_id INTEGER, file_path text, date timestamp, FOREIGN KEY(user_id) REFERENCES users (id))'
        cursor.execute(create_applications_table)

        create_events_table = 'CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, user_id INTEGER, event text, date timestamp, FOREIGN KEY(user_id) REFERENCES users (id))'
        cursor.execute(create_events_table)
        db.commit()
        db.close()
        return True
    except:
        return False
