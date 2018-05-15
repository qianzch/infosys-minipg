# -*- coding: utf-8 -*-
import hashlib
import web
import reply
import receive
import web
import thread
from log import REQ_TYPE, LOG

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
		if DEBUG:
			LOG.logi(req, REQ_TYPE.register)
		res = reply.RES_REGISTER('SUCCESS')
		return res.send()

	def handle_login(self, req):
		if DEBUG:
			LOG.logi(req, REQ_TYPE.login)
		res = reply.RES_LOGIN('SUCCESS')
		return res.send()

	def handle_select(self, req):
		if DEBUG:
			LOG.logi(req, REQ_TYPE.select)
		res = reply.RES_SELECT('SUCCESS')
		return res.send()

	def handle_like(self, req):
		if DEBUG:
			LOG.logi(req, REQ_TYPE.like)
		res = reply.RES_LIKE('SUCCESS')
		return res.send()