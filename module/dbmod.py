import pymysql

class database():
	def __init__(self):
		self.db = pymysql.connect(host='127.0.0.1', port=3333, user='developer', password='1234', db='bugbounty', charset='utf8')
		self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

	def execute(self, query, args={}):
		self.cursor.execute(query, args)

	def executeOne(self, query, args={}):
		self.cursor.execute(query, args)
		row = self.cursor.fetchone()
		return row

	def executeAll(self, query, args={}):
		self.cursor.execute(query, args)
		row = self.cursor.fetchall()
		return row

	def commit(self):
		self.db.commit()
