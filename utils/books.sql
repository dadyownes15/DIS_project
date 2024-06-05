DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE IF NOT EXISTS Books(
    subject_id int,
    subject_text varchar(50),
    isbn varchar(50),
    PRIMARY KEY (isbn)
);

DELETE FROM Books;


DROP TABLE IF EXISTS Syllabus;

CREATE TABLE IF NOT EXISTS Syllabus(
    subject_pk varchar(50) not null REFERENCES Courses(subject_text) ON DELETE CASCADE,
    isbn varchar(50) not null REFERENCES Books(isbn) ON DELETE CASCADE,
    semester_text varchar(50),
    PRIMARY KEY (subject_pk, isbn)
);

DELETE FROM Syllabus;

