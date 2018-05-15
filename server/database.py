# -*- coding: utf-8 -*-#
import MySQLdb
from log import LOG

class ERR():
	SUCCESS 		= 0
	ERR_UNKNOWN 	= 1
	USR_EXISTED 	= 11
	USR_NOT_EXISTS	= 12

	STR = {
		0:	'SUCCESS',
		1:	'ERR_UNKNOWN',
		11:	'USR_EXISTED',
		12: 'USR_NOT_EXISTS'
	}

class USR():

	def __init__(self):
		self.usr_name 	= ''
		self.passwd 	= ''
		self.wx_id 		= ''
		self.email 		= ''
		self.tel 		= ''
		self.likes 		= []

	# no security check here
	def construct_from_var(self, usr_name, passwd, wx_id, email, tel):
		self.usr_name 	= usr_name
		self.passwd 	= passwd
		self.wx_id 		= wx_id
		self.email 		= email
		self.tel 		= tel
		# one usr will not like anything if it is constructed from this call
		# self.likes	= likes

	def construct_from_sql(self, sql_obj):
		self.usr_name 	= sql_obj[0]
		self.passwd 	= sql_obj[1]
		self.wx_id 		= sql_obj[2]
		self.email 		= sql_obj[3]
		self.tel 		= sql_obj[4]
		# likes will be specially constructed

class INFO():

	def __init__(self):
		self.info_id 		= -1
		self.job_name 		= ''
		self.job_salary		= 0
		self.job_num 		= 0
		self.job_info 		= ''
		self.job_req 		= ''
		self.job_url 		= ''
		self.company_name	= ''
		self.company_info 	= ''
		self.company_url 	= ''
		self.apply_time 	= ''
		self.apply_tel 		= ''
		self.apply_email 	= ''
		self.attr_time 		= ''
		self.attr_expire 	= ''
		self.labels 		= []

	def construct(self, sql_obj):
		pass

# config
HOST		= '123.207.11.16'
USR_NAME	= 'infosys_dev'
USR_PASSWD	= 'softwareengineering'
DB_NAME		= 'infosys_minipg'

class DB():
	
	def __init__(self):
		self.db = None
		self.cursor = None

	def __del__(self):
		self.__close()

	def __connect(self):
		try:
			self.db = MySQLdb.connect(HOST, USR_NAME, USR_PASSWD, DB_NAME, charset = 'utf8')
			self.cursor = self.db.cursor()
		except Exception as e:
			LOG.loge(str(e))

	def __close(self):
		if self.db is not None:
			self.db.close()
			self.db = None

	def add_usr(self, usr):
		status = ERR.SUCCESS
		self.__connect()
		cmd = """
		insert into usr values(
			'{usr.usr_name}', '{usr.passwd}', '{usr.wx_id}', '{usr.email}', '{usr.tel}'
		)
		""".format(usr = usr)
		try:
			self.cursor.execute(cmd)
			self.db.commit()
		except Exception as e:
			self.db.rollback()
			status = ERR.USR_EXISTED
			LOG.loge(str(e))
		self.__close()
		return status

	# used for login
	def get_usr_by_name(self, usr_name):
		status = ERR.SUCCESS
		self.__connect()
		cmd = """
		select * from usr
		where usr_name = '{}'
		""".format(usr_name)
		usr = USR()
		try:
			self.cursor.execute(cmd)
			results = self.cursor.fetchall()
			if results:
				usr.construct_from_sql(results[0])
			else:
				status = ERR.USR_NOT_EXISTS
		except Exception as e:
			self.db.rollback()
			status = ERR.ERR_UNKNOWN
			LOG.loge(str(e))
		self.__close()
		return status, usr


db = DB()
#usr = USR()
#usr.construct_from_var('usr3', '123456', '', '', '')
status, usr = db.get_usr_by_name('user11')
print status, usr