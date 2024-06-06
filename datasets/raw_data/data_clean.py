import pandas as pd
import numpy as np

df = pd.read_csv('syllabus_data_29_04_2024.csv')


# Column headers
'''
'FETCH_DATE', 'SEMESTER_ID', 'SEMESTER_TEXT', 'UNIVERSITY_ID',
    'UNIVERSITY_TEXT', 'STUDY_ID', 'STUDY_TEXT', 'SUBJECT_ID',
    'SUBJECT_TEXT', 'ISBN'
'''

def format_csv_data(df):
    # Lowercase columns
    # Drop duplicates
    df = df.drop_duplicates()
    # Reset index
    df = df.reset_index(drop=True)
        #Define a Regex expression that matches where " - " is present in university_text
    regex = r' - .*| – .*'
    
    # Create a new column called university_name with the cleaned university names
    df['UNIVERSITY_TEXT'] = df['UNIVERSITY_TEXT'].str.replace(regex, '', regex=True)
    return df

def construct_major_database(df):
    # Construct major database, it includes University_ID, University_Text, Study_Id, Study_text
    major_db = df[['UNIVERSITY_TEXT', 'STUDY_TEXT']]
    major_db = major_db.drop_duplicates()
    # Lowercase columns
    major_db.columns = major_db.columns.str.lower()
    major_db = major_db.reset_index(drop=True)

    # Write out the major database to csv
    major_db.to_csv('majors_db.csv', index=False)

def construct_courses_database(df):
    # Construct Courses database, it includes Study_Id, Study_text, Subject_Id, Subject_text, Semester_Text, study_id, study_text
    courses_db = df[[ 'SUBJECT_TEXT','UNIVERSITY_TEXT']]
    courses_db = courses_db.drop_duplicates()
    # Lowercase columns
    courses_db.columns = courses_db.columns.str.lower()
    courses_db = courses_db.reset_index(drop=True)
    # Write out the courses database to csv
    courses_db.to_csv('courses_db.csv', index=False)

# counstruct books_database, it includes ISBN, Subject_Id, Subject_text

def construct_books_database(df):
    books_db = df[['ISBN']]
    books_db = books_db.drop_duplicates()
    # Lowercase columns
    books_db.columns = books_db.columns.str.lower()
    books_db = books_db.reset_index(drop=True)
    # Write out the books database to csv
    books_db.to_csv('books_db.csv', index=False)

def create_db(df_input):
    construct_major_database(df_input)
    construct_courses_database(df_input)
    construct_books_database(df_input)

def format_syllabus_data(df):
    syllabus_db = df[[ 'UNIVERSITY_TEXT', 'STUDY_TEXT', 'SUBJECT_TEXT','SEMESTER_TEXT','ISBN']]
    # Rename to lower case
    syllabus_db.columns = syllabus_db.columns.str.lower()
    syllabus_db = syllabus_db.drop_duplicates()
    syllabus_db = syllabus_db.reset_index(drop=True)

    
    # Write out the syllabus database to csv
    syllabus_db.to_csv('syllabus_db.csv', index=False)

def create_data():
    formated_df = format_csv_data(df)
    create_db(formated_df)
    format_syllabus_data(formated_df)
create_data()