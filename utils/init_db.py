# utils/init_db.py

import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
def get_db_connection():
     conn = psycopg2.connect(
        host="localhost"
    )
     return conn
def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            print("Creating major table")

            # Run SQL scripts
            with open('utils/majors.sql', 'r') as db_file:
                cur.execute(db_file.read())
                
            print("Creating courses table") 
            with open('utils/courses.sql', 'r') as db_file:
                cur.execute(db_file.read())
            print("Creating books table") 
            with open('utils/books.sql', 'r') as db_file:
                cur.execute(db_file.read())

            # Read and insert data majors
            print("Inserting data into Majors table")
            majors = pd.read_csv('datasets/majors_db.csv')

            for _, row in majors.iterrows():
                cur.execute(
                    "INSERT INTO Majors (university_text, study_text) VALUES ( %s, %s)",
                    ( row['university_text'], row['study_text'])
                ),

            # Read and insert data courses
            print("Inserting data into Courses table")
            courses = pd.read_csv('datasets/courses_db.csv').drop_duplicates()
            for _, row in courses.iterrows():
                cur.execute(
                    "INSERT INTO Courses (subject_text, university_text) VALUES ( %s, %s)",
                    ( row['subject_text'], row['university_text'])
                )
                # Read and insert data courses
            print("Inserting data into Books table")
            
            books = pd.read_csv('datasets/books_db.csv').drop_duplicates()
            
            for _, row in books.iterrows():
                cur.execute(
                    "INSERT INTO Books (isbn) VALUES (%s)",
                    (str(row['isbn']),)  # Ensuring ISBN is treated as a string
                )
            data = pd.read_csv('datasets/syllabus_db.csv')

            # Iterate through each row to insert data
            for index, row in data.iterrows():
                   cur.execute(
                        "INSERT INTO Curriculum (study_text, university_text, subject_text, semester_text) VALUES (%s, %s, %s, %s) ON CONFLICT (study_text, university_text, subject_text) DO NOTHING",
                        (row['study_text'], row['university_text'], row['subject_text'], row['semester_text'])
                    )
            for index, row in data.iterrows():
                try:
                    cur.execute(
                        "INSERT INTO Syllabus (subject_text, university_text, isbn) VALUES (%s, %s, %s) ON CONFLICT (subject_text, isbn, university_text) DO NOTHING",
                        (row['subject_text'], row['university_text'], row['isbn'])
                    )
                except Exception as e:
                    print(f"Error inserting data at row {index}: {e}")
                    
            conn.commit()
            
            
    finally:
        conn.close()

def query_db(query, args=(), one=False):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return (r[0] if r else None) if one else r