import sqlite3
import json
import os

DB_DIRECTORY = 'db_data'

def get_db_connection():
    conn = sqlite3.connect(os.path.join(DB_DIRECTORY,'glolf.sqlite'))
    conn.execute('pragma journal_mode=wal')
    return conn

def create_table_if_not_made(tablename):
    # WARNING: TABLENAME IS SQL INJECTABLE. DON'T ALLOW USER SUBMITTED TABLE NAMES
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
               (name text PRIMARY KEY NOT NULL, data text NOT NULL, version real)''')
    conn.commit()
    cursor.close()

def get_data(name, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE. DON'T ALLOW USER SUBMITTED TABLE NAMES
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename} WHERE name=?",(name, ))
    db_entry= cursor.fetchone()
    cursor.close()

    if db_entry is not None:
        player_name, player_data, version = db_entry
        return json.loads(player_data)

def set_data(name, data, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE
    version = 1
    data = json.dumps(data)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {tablename} VALUES (?, ?, ?)",(name, data, version))
    conn.commit()
    cursor.close()



# todo: replace with full sql scripts to avoid the tablename sql injection even though it's internal-only?
def create_player_table_if_not_made():
    create_table_if_not_made("players")

def get_player_data(name):
    create_player_table_if_not_made()
    return get_data(name, tablename="players")

def set_player_data(name, data):
    create_player_table_if_not_made()
    set_data(name, data, tablename="players")


def create_club_table_if_not_made():
    create_table_if_not_made("clubs")

def get_club_data(name):
    create_club_table_if_not_made()
    return get_data(name, tablename="clubs")

def set_club_data(name, data):
    create_club_table_if_not_made()
    set_data(name, data, tablename="clubs")
