import sqlite3
import json
import re
import uuuid

def connect_db():
    return sqlite3.connect('db/couch.db')


def build_full_house_obj(row):
    return { 'street': row[0],
             'name': row[1],
             'program': row[2],
             'quiet': row[3],
             'gradeR': row[4],
             'capacity': row[5],
             'description': row[6],
             'image': row[7],
             'geo': row[8],
             'uuid' : row[9],
             'wood' : row[10],
             'savailable' : row[11],
             'davailable' : row[12],
             'tavailable' : row[13],
             'qavailable' : row[14],
             'rooms' : row[15]
            }
def build_house_obj(row):
    street = row[0]
    name = row[1]
    program = row[2]
    quiet = row[3]
    uuid.uuid1() = row [4]
    priority = row[5]

    return {'id': street, 'dorm': name, 'code': code, 'quiet': quiet, 'uuid': uuid, 'priority' : priority}

def build_full_section_obj(row):
	return { 'street': row[0],
	'numvacancies': row[1],
	'permissionRequired': row[2],
	'gradeR': row[3],
	'savailable': row[4],
	'davailable': row[5],
	'tavailable': row[6],
	'qavailable': row[7],
	'rooms': row[8],
	'uuid' : row[9]
	}

def HouseMouse(res):
    ret = []
    for result in res:
        ret.append(build_house_obj(result))
    return ret
#this adds the room/house selected to the list of houses that have been selected

def HouseKeyword(conn, term):
    c = conn.cursor()
    return c.execute("""
      select _uid from courses
      where (lower(street) like lower("""+json.dumps("%"+term+"%")+""") or lower(program) like lower("""+json.dumps('%'+term+'%')+"""))or lower(name) like lower("""+json.dumps('%'+term+'%')+"""))""") 

def getGradR(conn, courseid):
    c = conn.cursor()
    return c.execute("select _uid from sections where course_uid = " + str(courseid))