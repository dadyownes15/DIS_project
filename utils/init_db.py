# utils/init_db.py

import psycopg2
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def init_db():
    conn = psycopg2.connect(
        host="localhost",
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
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

            # Read and insert data
            majors = pd.read_csv('utils/majors_db.csv')
            majors = majors.rename(columns={
                'UNIVERSITY_ID': 'university_id', 
                'UNIVERSITY_TEXT': 'university_text', 
                'STUDY_ID': 'study_id', 
                'STUDY_TEXT': 'study_text'
            })
            for _, row in majors.iterrows():
                cur.execute(
                    "INSERT INTO Majors (university_id, university_text, study_id, study_text) VALUES (%s, %s, %s, %s)",
                    (row['university_id'], row['university_text'], row['study_id'], row['study_text'])
                )
            conn.commit()
    finally:
        conn.close()
