from flask_sqlalchemy import SQLAlchemy
import psycopg2, csv 

db = SQLAlchemy()


#aufrufen der methode connect zur Verbindung mit der PostgreSQL DB
conn = psycopg2.connect(
  database="project1",
  user="postgres",
  host="localhost",
  port="5432"
  )

cur = conn.cursor()

class test(db.Model):
  __tablename__ = 'test'
  id = db.Column(db.Integer, primary_key = True)
  userid = db.Column(db.String(50))
  floor = db.Column(db.String(50))
  room = db.Column(db.String(50))
  status = db.Column(db.String(50))

class users(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100), unique=True)
  role = db.Column(db.String(100))
  projectname = db.Column(db.String(100))

	
  def __init__(self, username, password, role, projectname):
     #Attribute der Klasse -> self.xxxx
    self.username = username
    self.password = password 
    self.role = role 
    self.projectname = projectname


class projects(db.Model):
  __tablename__ = 'projects'
  id = db.Column(db.Integer, primary_key = True)
  projectname = db.Column(db.String(100))
  filename = db.Column(db.String(100))


class rooms(db.Model):
  __tablename__ = 'rooms'
  id = db.Column(db.Integer, primary_key = True)
  userid = db.Column(db.String(100))
  floor = db.Column(db.String(100))
  room = db.Column(db.String(100))
  status = db.Column(db.String(100))

  def __init__(self, userid, floor, room, status):
    self.userid = userid
    self.floor = floor 
    self.room = room 
    self.status = status



 

conn.close()