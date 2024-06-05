DROP TABLE IF EXISTS Courses CASCADE;

CREATE TABLE IF NOT EXISTS Courses(
    study_id int,
    study_text varchar(50),
    subject_id int,
    subject_text varchar(50),
    semester_text varchar(50),
    PRIMARY KEY (subject_text)
);

DELETE FROM Courses;

DROP TABLE IF EXISTS Curriculum;

CREATE TABLE IF NOT EXISTS Curriculum(
    study_pk VARCHAR(50) NOT NULL REFERENCES Majors(study_text) ON DELETE CASCADE,
    subject_pk VARCHAR(50) NOT NULL REFERENCES Courses(subject_text) ON DELETE CASCADE,
    semester_text VARCHAR(50),
    PRIMARY KEY (study_pk, subject_pk)
);
