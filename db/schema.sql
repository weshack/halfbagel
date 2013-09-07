DROP TABLE IF EXISTS residences;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS selections;

CREATE TABLE residences (
_uid INTEGER PRIMARY KEY,
location TEXT,
image TEXT,
description TEXT,
program INTEGER,
quiet INTEGER,
wood INTEGER,
units INTEGER,
restriction INTEGER,
geo_x REAL,
geo_y REAL
);

CREATE TABLE rooms (
_uid INTEGER PRIMARY KEY,
residence_id INTEGER,
room_number INTEGER,
size INTEGER,
FOREIGN KEY(residence_id) REFERENCES residences(_uid)
);

CREATE TABLE groups (
_uid INTEGER PRIMARY KEY,
name TEXT,
size INTEGER
);

CREATE TABLE students (
_uid INTEGER PRIMARY KEY,
group_id INTEGER,
student_id TEXT,
forename TEXT,
surname TEXT,
FOREIGN KEY(group_id) REFERENCES groups(_uid)
);

CREATE TABLE selections (
_uid INTEGER PRIMARY KEY,
priority INTEGER,
group_id INTEGER,
room_id INTEGER,
student_id INTEGER,
FOREIGN KEY(group_id) REFERENCES groups(_uid),
FOREIGN KEY(room_id) REFERENCES rooms(_uid),
FOREIGN KEY(student_id) REFERENCES students(_uid)
);
