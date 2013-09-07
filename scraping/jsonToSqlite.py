import sqlite3
import json

# json_data = open("residences.json")
conn = sqlite3.connect("../db/grs.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS residences")
c.execute("DROP TABLE IF EXISTS rooms")
c.execute("DROP TABLE IF EXISTS groups")
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS selections")

c.execute("CREATE TABLE residences (_uid INTEGER PRIMARY KEY, location TEXT, image TEXT, " + 
	"description TEXT, program INTEGER, quiet INTEGER, wood INTEGER, units INTEGER, " +
	"restriction INTEGER, geo_x REAL, geo_y REAL)")

c.execute("CREATE TABLE rooms (_uid INTEGER PRIMARY KEY, residence_id INTEGER, " +
	"room_number INTEGER, size INTEGER, FOREIGN KEY (residence_id) REFERENCES residences(_uid))")

c.execute("CREATE TABLE groups (_uid INTEGER PRIMARY KEY, name TEXT, size INTEGER)")

c.execute("CREATE TABLE students (_uid INTEGER PRIMARY KEY, group_id INTEGER, " + 
	"student_id TEXT, forename TEXT, surname TEXT, FOREIGN KEY(group_id) REFERENCES groups(_uid))")

c.execute("CREATE TABLE selections (_uid INTEGER PRIMARY KEY, priority INTEGER, " +
	"group_id INTEGER, room_id INTEGER, student_id INTEGER, FOREIGN KEY(group_id) REFERENCES groups(_uid), " + 
	"FOREIGN KEY(room_id) REFERENCES rooms(_uid), FOREIGN KEY(student_id) REFERENCES students(_uid)" + 
	")")
