# -*- coding: utf-8 -*-# 
import xml.etree.ElementTree as ET

def parse_xml(web_data):
	if len(web_data) == 0:
		return None
	xml_data = ET.fromstring(web_data)
	req_type = xml_data.find('ReqType').text
	if req_type == 'register':
		return REQ_REGISTER(xml_data)
	elif req_type == 'login':
		return REQ_LOGIN(xml_data)
	elif req_type == 'select':
		return REQ_SELECT(xml_data)
	elif req_type == 'like':
		return REQ_LIKE(xml_data)
	return None

class REQ_DATA():
	def __init__(self, xml_data):
		self.req_type = xml_data.find('ReqType').text
		
class REQ_REGISTER(REQ_DATA):
	def __init__(self, xml_data):
		REQ_DATA.__init__(self, xml_data)
		self.usr_name	= xml_data.find('UsrName').text
		self.passwd		= xml_data.find('Passwd').text
		self.email		= xml_data.find('Email').text
		self.tel		= xml_data.find('Tel').text
		
class REQ_LOGIN(REQ_DATA):
	def __init__(self, xml_data):
		REQ_DATA.__init__(self, xml_data)
		self.usr_name	= xml_data.find('UsrName').text
		self.passwd		= xml_data.find('Passwd').text
		
class REQ_SELECT(REQ_DATA):
	def __init__(self, xml_data):
		REQ_DATA.__init__(self, xml_data)
		self.ids		= [i.text for i in xml_data.find('Ids').findall('Id')]
		self.labels		= [i.text for i in xml_data.find('Labels').findall('Label')]
		self.keywords	= [i.text for i in xml_data.find('Keywords').findall('Keyword')]
		self.method		= xml_data.find('Method').text

class REQ_LIKE(REQ_DATA):
	def __init__(self, xml_data):
		REQ_DATA.__init__(self, xml_data)
		self.usr_name	= xml_data.find('UsrName').text
		self.id			= xml_data.find('Id').text
		self.get_noti	= xml_data.find('GetNoti').text