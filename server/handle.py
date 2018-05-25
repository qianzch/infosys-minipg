# -*- coding: utf-8 -*-
import hashlib
import web
import reply
import receive
import web
import thread
import traceback
from log import REQ_TYPE, LOG
from database import DB, ERR, USR, INFO

DEBUG = True

class Handle():
	def GET(self):
		return 'DO NOT USE METHOD \"GET\" !'

	def POST(self):
		try:
			web_data = web.data()
			#print 'Handle Post webdata is ', web_data, '\n\n' # print log in server
			req = receive.parse_xml(web_data)
			
			if isinstance(req, receive.REQ_DATA) and req.req_type == 'register':
				return self.handle_register(req)
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'login':
				return self.handle_login(req)
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'select':
				return self.handle_select(req)
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'like':
				return self.handle_like(req)
			
			print 'NOT HANDLED !'
			return 'success'
		except Exception, Argment:
			return Argment

	def handle_register(self, req):
		usr = USR()
		usr.construct_from_req(req)
		status = DB().add_usr(usr)
		if DEBUG and not status == ERR.SUCCESS:
			LOG.loge(ERR.STR[status])
			LOG.logi(req, REQ_TYPE.register)
		res = reply.RES_REGISTER(ERR.STR[status])
		return res.send()

	def handle_login(self, req):
		status, usr = DB().get_usr_by_name(req.usr_name)
		if DEBUG and not status == ERR.SUCCESS:
			LOG.loge(ERR.STR[status])
			LOG.logi(req, REQ_TYPE.login)
		sta_str = ERR.STR[status] if usr.passwd == req.passwd else 'INVALID PASSWD'
		res = reply.RES_LOGIN(sta_str)
		return res.send()

	def handle_select(self, req):
		status, infos = DB().get_info_by_req(req)
		if DEBUG and not status == ERR.SUCCESS:
			LOG.loge(ERR.STR[status])
			LOG.logi(req, REQ_TYPE.select)
		if status == ERR.SUCCESS:
			status_label, infos = DB().set_infos_labels(infos)
			if DEBUG and not status == ERR.SUCCESS:
				LOG.loge(ERR.STR[status_label])
				LOG.logi(req, REQ_TYPE.select)
		res = reply.RES_SELECT(ERR.STR[status], infos)
		return res.send()

	def handle_like(self, req):
		if DEBUG:
			LOG.loge(ERR.STR[status])
			LOG.logi(req, REQ_TYPE.like)
		res = reply.RES_LIKE('SUCCESS')
		return res.send()