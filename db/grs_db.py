import sqlite3
import json
import re

conn = sqlite3.connect('db/couch.db')

def build_residence_obj(row):
    return { 
    '_uid' : row[0],   
    'location': row[1]
    'program' : row[2],
    'quiet' : row[3],
    'restriction' : row[4],
    'rooms' : row[5],
    'description' : row[6],
    'image' : row[7],
    'geo_x' : row[8],
    'geo_y' : row[9],
    'wood' : row[10]
    }

def build_room_obj(row):
    return {
    '_uid': row[0],
    'residence_id': row[1],
    'room_number': row[2],
    'capacity': row[3]
    }

def build_group_obj(row):
    return {
    '_uid': row[0],
    'name': row[1],
    'size': row[2]
    }

def build_student_obj(row):
    return {
    '_uid': row[0],
    'group_id': row[1],
    'student_id': row[2],
    'forename': row[3],
    'surname': row[4]
    }

def build_selection_obj(row):
    return {
    '_uid': row[0],
    'group_id': row[1],
    'room_id': row[2],
    'priority': row[3]
    }

def get_all_residences():
    ret {}
    c = conn.cursor()
    for residenceid in range(int(c.execute("select COUNT(*) from residence").next()[0])):
        residence = get_residence_summary(conn, residenceid)
    return c.execute('select * from residence')

def get_residence(conn, residenceid):
    c = conn.cursor()
    residence = build_residence_obj(c.execute("select * from residence where _uid = " + str(residenceid)).next())
    return residence

