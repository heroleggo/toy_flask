import pymysql

class database():
	def __init__(self):
		self.db = pymysql.connect(host='localhost', port=3306, user='root', password='qpqpqpqp1', db='develop', charset='utf8')
		print self.db
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
