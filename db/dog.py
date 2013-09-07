import flask from Flask, request
import random, json

 import smtplib  




@app.route("/groups/create")
def createGroup():
    conn = sqlite3.connect("../db/grs.db")
    c = conn.cursor()

    email = request.args.get('email', '')
    groupid = random_with_N_digits(6)
    c.execute("INSERT INTO groups VALUES(groupid,email,1)")
    conn.commit()


    #database stuff, or maybe editing JSON file by Python
 
 
@app.route("/groups/join")
def joinGroup():
    conn = sqlite3.connect("/groups/create.db")
    c = conn.cursor()

    email = request.args.get('email', '')
    groupid = request.args.get('groupid', '')
    
    sql = """
    UPDATE albums 
    SET size = size ++ 
    WHERE groupid = groupid"""
    cursor.execute(sql)
    conn.commit()

    #database stuff, or maybe editing JSON file by Python
 
 
@app.route("/rooms/final")
def finalizeRooms():
    email = request.args.get('groupid', '')
    selectedRooms = request.args.get('selected', '')
    conn = sqlite3.connect("../db/grs.db")
    c = conn.cursor()
    cursor.execute()
    val = c.execute("SELECT student_id FROM student WHERE groupid = " + str(groupid)).next())
    email(val,"room selected"+ c.execute("SELECT room_id FROM selection WHERE groupid = " + str(groupid)).next())
    #JSON parsing for selectedRooms variable
  
def email(email,text):
    fromaddr = 'developer.halfbagel@gmail.com'  
    toaddrs  = email

    TEXT = text  
    SUBJECT = 'HELLO,WORLD'
    msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)

    # Credentials (if needed)  
    username = 'developer.halfbagel@gmail.com'  
    password = 'weshack2013'  
  
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromaddr, toaddrs, msg)  
    server.quit()  

    #database stuff, or maybe editing JSON file by Py