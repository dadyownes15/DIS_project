DROP TABLE IF EXISTS Courses CASCADE;

CREATE TABLE IF NOT EXISTS Courses(
    subject_text varchar(50),
    university_text varchar(50),
    PRIMARY KEY (subject_text, university_text)
);


DROP TABLE IF EXISTS Curriculum;

CREATE TABLE IF NOT EXISTS Curriculum(
    study_text VARCHAR(50) NOT NULL,
    university_text VARCHAR(50) NOT NULL,
    subject_text VARCHAR(50) NOT NULL,
    semester_text VARCHAR(50),
    PRIMARY KEY (study_text, university_text, subject_text),
    FOREIGN KEY (study_text, university_text) REFERENCES Majors(study_text, university_text) ON DELETE CASCADE,
    FOREIGN KEY (subject_text, university_text) REFERENCES Courses(subject_text, university_text) ON DELETE CASCADE
);
