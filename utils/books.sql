DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE IF NOT EXISTS Books(
    isbn varchar(50),
    PRIMARY KEY (isbn)
);

DELETE FROM Books;


DROP TABLE IF EXISTS Syllabus;

CREATE TABLE IF NOT EXISTS Syllabus(
    subject_text varchar(50),
    university_text varchar(50),
    isbn varchar(50),
    PRIMARY KEY (subject_text, isbn, university_text),
    FOREIGN KEY (subject_text, university_text) REFERENCES Courses(subject_text, university_text) ON DELETE CASCADE,
    FOREIGN KEY (isbn) REFERENCES Books(isbn) ON DELETE CASCADE
);

DELETE FROM Syllabus;

