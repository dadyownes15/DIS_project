# DIS_project

## Team Members
- QKG434 - Peter Østergård
- XDG178 - Mikkel Dahl

## Description
Final project for the course "Database and Information Systems" at the University of Copenhagen, DIKU department.



## Initialisation procedure
Clone / download repository files and run the following to install the required packages (within a venv):
```
    pip install -r requirements.txt
```

Create a new database in pgAdmin (preferably named BOOKS) and add the following to your .env file (normally
.env should be a private file containing user secrets, in this case we have kept it inside the project files for easy
access for the TAs):

```
    SECRET_KEY=<secret_key>
    DB_USERNAME=postgres || <postgres_user_name>
    DB_PASSWORD=<postgres_user_password>
    DB_NAME=BOOKS || <postgres_db_name>
```


## Running Our Curriculum Finder

1. **Set Up Your Working Directory**
   - Navigate to the `DIS_project` directory and make sure it is your current working directory.

2. **Start the Application**
   - Open your terminal and run the following command:
     ```
     flask run
     ```
   - This command sets up all necessary tables, loads data into them, and starts the web server.

3. **Access the Web Interface**
   - Once the server is running, access the application through your web browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Navigating Our Beautiful Website

Our website is designed to be straightforward and easy to use:
1. **Select a University:** Choose a university from the list provided.
2. **Choose a Major:** After selecting a university, you will be prompted to select a major.
3. **Pick a Semester:** Select the semester for which you want to view courses.
4. **View Courses and Materials:** You will receive a list of courses along with the ISBNs for required reading materials for each course.

## Utilizing Regex

We have employed regex to clean and standardize the university names in our dataset. The relevant code can be found in the `data_clean` module, as shown below:

```python
regex = r' - .*| – .*'

# Create a new column called university_name with the cleaned university names
df['UNIVERSITY_TEXT'] = df['UNIVERSITY_TEXT'].str.replace(regex, '', regex=True)
```

This regex removes any text following a dash (' - ' or ' – ') in the university names, simplifying and standardizing the data for easier processing.