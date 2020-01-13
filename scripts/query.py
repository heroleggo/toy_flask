import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from module import dbmod

def signup(data):
	db = dbmod.database()
	d1 = data['email']
	d2 = data['username']
	d3 = data['password']
	s = "SELECT * FROM info WHERE `username`=%s"
	r = db.executeOne(s, d2)
	if r:
		return "duplicated"
	else:
		s2 = "INSERT INTO info(username, password, email) VALUES('{0}', '{1}', '{2}')".format(d2, d3, d1)
		print "query : "+ (s2)
		r2 = db.executeOne(s2)
		print (r2)
		if r2:
			db.commit()
			return "success"
		else:
			return "fail"

def signin(data):
	db = dbmod.database()
	d1 = data['username']
	d2 = data['password']
	s = "SELECT * FROM info WHERE `username`='{0}' and `password`='{1}'".format(d1, d2)
	r = db.executeOne(s)
	if r:
		return "success"
	else:
		return "fail"
