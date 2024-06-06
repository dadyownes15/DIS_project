DROP TABLE IF EXISTS Majors CASCADE;

CREATE TABLE IF NOT EXISTS Majors(
    study_text varchar(50),
    university_text varchar(50),
    PRIMARY KEY (study_text, university_text)
);

DELETE FROM Majors;
