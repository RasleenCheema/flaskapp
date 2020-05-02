from settings import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from datetime import datetime
#from flask_mongoengine  import model_form


class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(60) )
	email = db.Column(db.String(60))
	password = db.Column(db.String(500))
	mobile_number = db.Column(db.String(300))
	create_at = db.Column(
			db.TIMESTAMP,
			default=datetime.utcnow,
			nullable=False
		)


#class User(mongo.Document):
#	id = mongo.Column(mongo.Integer, primary_key=True)
#	name = mongo.Column(mongo.String(60))
#	email = mongo.Column(mongo.String(60))
#	password = mongo.Column(mongo.String(500))
#	mobile_number = mongo.Column(mongo.String(300))
#	create_at = db.Column(
#			db.TIMESTAMP,
#			default=datetime.utcnow,
#			nullable=False
#	)

	def __str__(self):
		return self.name + self.email + str(self.mobile_number)
