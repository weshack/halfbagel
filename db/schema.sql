CREATE TABLE residence (
_uid INTEGER PRIMARY KEY,
location TEXT,
program INTEGER,
quiet INTEGER,
restriction INTEGER,
description TEXT,
image TEXT,
geo_x REAL,
geo_y REAL,
wood INTEGER, 
units INTEGER
)

CREATE TABLE room (
_uid INTEGER PRIMARY KEY,
FOREIGN KEY(residence_id) REFERENCES residence(_uid),
room_number INTEGER,
size INTEGER
)

CREATE TABLE group (
_uid INTEGER PRIMARY KEY,
name TEXT,
size INTEGER
)

CREATE TABLE student (
_uid INTEGER PRIMARY KEY,
FOREIGN KEY(group_id) REFERENCES group(_uid),
student_id TEXT,
forename TEXT,
surname TEXT
)

CREATE TABLE selection (
_uid INTEGER PRIMARY KEY,
FOREIGN KEY(group_id) REFERENCES group(_uid),
FOREIGN KEY(room_id) REFERENCES group(_uid),
FOREIGN KEY(student_id) REFERENCES group(_uid),
priority INTEGER
)
