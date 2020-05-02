import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from flask_pymongo import PyMongo

#from flask_mongoengine import MongoEngine

#db = MongoEngine()

db_dir = os.path.abspath('data.sqlite')

app = Flask(__name__)

#db = MySQL()
app.config['SECRET_KEY'] = 'you-will-never-guess'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rasu@localhost/mydb'
# db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+db_dir
db = SQLAlchemy(app)
#mysql username and passs    rasleencheema     rasu

app.config['MONGO_DBNAME'] = 'mongodatabase'
app.config["MONGO_URI"] = "mongodb://localhost:27017/mongodatabase"
mongo = PyMongo(app)