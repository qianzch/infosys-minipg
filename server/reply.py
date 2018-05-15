# -*- coding: utf-8 -*-# 
import time

# ref: http://www.runoob.com/python/python-mysql.html

class RES_DATA():
	def __init__(self):
		pass
	def send(self):
		return 'SUCCESS'

class RES_REGISTER(RES_DATA):
	def __init__(self, err_info):
		self.__dict = dict()
		self.__dict['ErrInfo'] = err_info
	def send(self):
		XmlForm = """
		<xml>
		<ErrInfo><![CDATA[{ErrInfo}]]></ErrInfo>
		</xml>
		"""
		return XmlForm.format(**self.__dict)

class RES_LOGIN(RES_DATA):
	def __init__(self, err_info):
		self.__dict = dict()
		self.__dict['ErrInfo'] = err_info
	def send(self):
		XmlForm = """
		<xml>
		<ErrInfo><![CDATA[{ErrInfo}]]></ErrInfo>
		</xml>
		"""
		return XmlForm.format(**self.__dict)

class RES_SELECT(RES_DATA):
	def __init__(self, err_info):
		self.__dict = dict()
		self.__dict['ErrInfo'] = err_info
	def send(self):
		XmlForm = """
		<xml>
		<ErrInfo><![CDATA[{ErrInfo}]]></ErrInfo>
		</xml>
		"""
		#for i in self.dlist:
		#	XmlForm += '<List><![CDATA[{}]]></List>'.format(i)
		return XmlForm.format(**self.__dict)

class RES_LIKE(RES_DATA):
	def __init__(self, err_info):
		self.__dict = dict()
		self.__dict['ErrInfo'] = err_info
	def send(self):
		XmlForm = """
		<xml>
		<ErrInfo><![CDATA[{ErrInfo}]]></ErrInfo>
		</xml>
		"""
		return XmlForm.format(**self.__dict)