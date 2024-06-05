#database initialisation
import os
from flask import Flask
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

conn = psycopg2.connect(
    host="localhost",
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD')
)

#Helps formatting the data retrieved from the database
db_cursor = conn.cursor(cursor_factory=RealDictCursor)
