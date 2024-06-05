from flask import Flask
from DIS_project.utils.init_db import init_db
 # Adjust the import path based on your project structure

app = Flask(__name__)

#Load database
init_db()

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
    
