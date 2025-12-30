import sqlite3
import pandas as pd

DB_NAME = 'student_list.db'

def init_db():
    '''
    Initializing the DB
    '''
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            state TEXT,
            subjects TEXT
        )
''')
    conn.commit()
    conn.close()

def add_student(name, age, gender, state, subjects):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    sub_str = ','.join(subjects)
    c.execute('INSERT INTO students (name, age, gender, state, subjects) VALUES (?,?,?,?,?)',
              (name, age, gender, state, sub_str))
    conn.commit()
    conn.close()

def get_all_students():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    df = pd.read_sql_query('SELECT * FROM students', conn)
    conn.close()
    return df

def delete_student(student_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM studentS WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

