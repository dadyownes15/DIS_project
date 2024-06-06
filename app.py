from flask import Flask, render_template, request, jsonify
from DIS_project.utils.init_db import init_db, query_db, get_db_connection  # Ensure you have a function to execute queries

app = Flask(__name__)

# Load database
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.form)
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST' and 'university' in request.form:
        # Fetch majors for the selected university
        
        university_text = request.form['university']
        print("Fetch all majors from the selected " + university_text)
        cur.execute('SELECT * FROM Majors WHERE university_text = %s', (university_text,))
        majors = cur.fetchall()
        cur.close()
        return render_template('majors.html', majors=majors, university=university_text)
    if request.method == 'POST' and 'major' in request.form:
        print("MAJOR")
        # Fetch courses for the selected university
        major_text = request.form['major']
        university_text = request.form['university_hidden']
        print("MAJOR TEXT", major_text)
        print("UNIVERSITY TEXT", university_text)
        cur.execute('SELECT DISTINCT(semester_text) FROM Curriculum WHERE university_text = %s AND study_text = %s', (university_text,major_text))
        
        semesters_text = cur.fetchall()
        print("SEMESTERS TEXT", semesters_text)
        cur.close()
        return render_template('courses.html', semester_text=semesters_text, university=university_text, major=major_text)
    if request.method == 'POST' and 'semester' in request.form:
        # Fetch syllabus for the given major and semester
        semester_text = request.form['semester']
        major_text = request.form['major_hidden']
        university_text = request.form['university_hidden']
        cur.execute('SELECT DISTINCT(subject_text) FROM Curriculum WHERE university_text = %s AND study_text = %s AND semester_text = %s', (university_text, major_text, semester_text))
        subjects = cur.fetchall()
        
        print("SUBJECTS", subjects)
        
        #Create a result dictionary where the key is the subject_text and the value is a list of books
        results = {}
        
        #For each subject_text, fetch the books
        
        
        #For each subject_text, fetch the books
        for subject in subjects:
            cur.execute('SELECT isbn FROM Syllabus WHERE university_text = %s AND subject_text = %s', (university_text, subject[0]))
            books = cur.fetchall()
            # Add the books to the results dictionary
            results[subject[0]] = books
        
        print("RESULTS", results)
        cur.close()
        return render_template('syllabus.html', university=university_text, major=major_text, semester=semester_text, subject_books=results)
    
    else:
        # Load the initial university selection form
        cur.execute('SELECT DISTINCT university_text FROM Majors')
        universities = cur.fetchall()
        cur.close()
        return render_template('index.html', universities=universities)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/fetch_books', methods=['POST'])
def fetch_books():
    # Perform the SQL query
    results = query_db("SELECT b.isbn FROM Books b JOIN Syllabus s ON b.isbn = s.isbn JOIN Courses c ON s.subject_text = c.subject_text AND s.university_text = c.university_text WHERE c.subject_text = %s AND c.university_text = %s;", ('BSc BLC Area Studies 2 - German: Markets, institut', 'CBS - Copenhagen Business School'))
    if results:
        return jsonify(results)  # Send results back as JSON
    else:
        return "No books found for this course at the specified university."

if __name__ == '__main__':
    app.run(debug=True)
