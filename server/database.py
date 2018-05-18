# -*- coding: utf-8 -*-#
import MySQLdb
from log import LOG

class ERR():
	SUCCESS 			= 0
	ERR_UNKNOWN 		= 1
	USR_EXISTED 		= 11
	USR_NOT_EXISTS		= 12
	ALREADY_LIKED 		= 13
	LIKES_NOT_EXIST 	= 14
	SOME_ID_NOT_EXISTS	= 15
	EMPTY_SELECT_REQ 	= 16

	STR = {
		0:	'SUCCESS',
		1:	'ERR_UNKNOWN',
		11:	'USR_EXISTED',
		12:	'USR_NOT_EXISTS',
		13:	'ALREADY_LIKED',
		14:	'LIKES_NOT_EXIST',
		15:	'SOME_ID_NOT_EXISTS',
		16:	'EMPTY_SELECT_REQ'
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
		
	def construct_from_sql(self, sql_obj):
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

	# register
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

	# login
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
			status = ERR.ERR_UNKNOWN
			LOG.loge(str(e))
		self.__close()
		return status, usr
	
	# insert like
	def add_usr_like(self, usr_name, info_id):
		status = ERR.SUCCESS
		self.__connect()
		cmd = """
		insert into usr_like values(
			'{0}', '{1}'
		)
		""".format(usr_name, info_id)
		try:
			self.cursor.execute(cmd)
			self.db.commit()
		except Exception as e:
			self.db.rollback()
			status = ERR.ALREADY_LIKED
			LOG.loge(str(e))
		self.__close()
		return status
	
	# get likes
	def get_usr_likes_by_name(self, usr_name):
		status = ERR.SUCCESS
		self.__connect()
		cmd = """
		select * from usr_like
		where usr_name = '{}'
		""".format(usr_name)
		likes = []
		try:
			self.cursor.execute(cmd)
			results = self.cursor.fetchall()
			if results:
				for e in results:
					likes.append(e[1])
			else:
				status = ERR.LIKES_NOT_EXIST
		except Exception as e:
			status = ERR.ERR_UNKNOWN
			LOG.loge(str(e))
		self.__close()
		return status, likes
		
	# remove like
	def remove_usr_like(self, usr_name, info_id):
		status = ERR.SUCCESS
		self.__connect()
		cmd = """
		delete from usr_like
		where usr_name = '{0}' and info_id = '{1}'
		""".format(usr_name, info_id)
		try:
			self.cursor.execute(cmd)
			db.commit()
		except Exception as e:
			self.db.rollback()
			status = ERR.LIKES_NOT_EXIST
			LOG.loge(str(e))
		self.__close()
		return status
	
	def __get_info_by_ids(self, ids):
		status = ERR.SUCCESS
		self.__connect()
		infos = []
		for e in ids:
			cmd = """
			select * from info
			where info_id = '{}'
			""".format(e)
			try:
				self.cursor.execute(cmd)
				results = self.cursor.fetchall()
				if results:
					info = INFO()
					info.construct_from_sql(results[0])
					infos.append(info)
				else:
					status = ERR.SOME_ID_NOT_EXISTS
			except Exception as e:
				status = ERR.ERR_UNKNOWN
				LOG.loge(str(e))
		self.__close()
		return status, infos
		
	def __get_info_by_labels(self, labels):
		status = ERR.SUCCESS
		self.__connect()
		infos = []
		for e in labels:
			cmd = """
			select * from info
			where info_id = '{}'
			""".format(e)
			try:
				self.cursor.execute(cmd)
				results = self.cursor.fetchall()
				if results:
					info = INFO()
					info.construct_from_sql(results[0])
					infos.append(info)
				else:
					status = ERR.SOME_ID_NOT_EXISTS
			except Exception as e:
				status = ERR.ERR_UNKNOWN
				LOG.loge(str(e))
		self.__close()
		return status, infos
		
	def __get_info_by_keywds(self, keywds):
		return ERR.ERR_UNKNOWN, []

	def __get_info_by_labels_keywds(self, labels, keywds):
		status = ERR.SUCCESS
		self.__connect()
		infos = []
		keywords = keywds 
		return ERR.ERR_UNKNOWN, []

	# get info
	def get_info_by_req(self, req_select):
		# see 'receive.py' for more info about 'req_select'
		status = ERR.EMPTY_SELECT_REQ
		infos = []
		keywds = req_select.keywords.strip() # split here
		# if ids are given, then select info use ONLY ids
		if len(req_select.ids) > 0:
			return self.__get_info_by_ids(req_select.ids)
		if len(req_select.labels) > 0:
			status, infos = self.__get_info_by_labels(req_select.labels)
			if not status == ERR.SUCCESS:
				return status, infos
		if not keywds == '':
			if len(req_select.labels) > 0:
				return self.__get_info_by_labels_keywds(req_select.labels, keywds)
			else:
				return self.__get_info_by_keywds(keywds)
		return status, infos




db = DB()
#usr = USR()
#usr.construct_from_var('usr3', '123456', '', '', '')
status, usr = db.get_usr_by_name('user11')
print status, usr