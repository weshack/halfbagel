import sqlite3
import json
import re

conn = sqlite3.connect('db/grs.db')

def build_residence_obj(row):
    return { 
    'id' : row[0],   
    'location': row[1]
    'program' : row[2],
    'quiet' : row[3],
    'restriction' : row[4],
    'description' : row[5],
    'image' : row[6],
    'geo_x' : row[7],
    'geo_y' : row[8],
    'wood' : row[9]
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

def get_all_residences(conn):
    residences = {}
    c = conn.cursor()
    for residence_id in range(int(c.execute("SELECT COUNT(*) FROM residences").next()[0])):
        residence = get_residence_by_id(conn, residence_id)
        residences[residence['id']] = residence
    return ret

def get_residences_by_unit_size(conn, unit_size):
    residences = {}
    c = conn.cursor()
    for residence_id in range(int(c.execute("SELECT COUNT(*) FROM residences").next()[0])):
        residence = get_residence_by_id(conn, residence_id)
        if residence['units'] == unit_size:
            residences[residence['id']] = residence
    return residences

def get_residences_by_wood_status(conn, wood_status):
    residences = {}
    c = conn.cursor()
    for residence_id in range(int(c.execute("SELECT COUNT(*) FROM residences").next()[0])):
        residence = get_residence_by_id(conn, residence_id)
        if residence['wood'] == 1:
            residences[residence['id']] = residence
    return residences

def get_residence_by_id(conn, residence_id):
    c = conn.cursor()
    residence = build_residence_obj(c.execute("SELECT * FROM residences WHERE _uid = " + str(residence_id)).next())
    return residence

def get_residence_by_location(conn, term):
    c = conn.cursor()
    return c.execute("""SELECT _uid FROM residences WHERE (lower(name) LIKE lower(""" + json.dumps("%"+term+"%")+ """))""")

def get_room_by_size(conn, size):
    c = conn.cursor()
    return c.execute("SELECT _uid FROM rooms WHERE size = " + str(size)).next())