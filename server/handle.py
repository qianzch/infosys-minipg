# -*- coding: utf-8 -*-
import hashlib
import web
import reply
import receive
import web
import thread

class Handle(object):
	def GET(self):
		return 'DO NOT USE METHOD \"GET\" !'

	def POST(self):
		try:
			web_data = web.data()
			print 'Handle Post webdata is ', web_data, '\n\n' # print log in server
			req = receive.parse_xml(web_data)
			
			if isinstance(req, receive.REQ_DATA) and req.req_type == 'register':
				return self.handle_register(req)
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'login':
				res = self.handle_login(req)
				if not res == None:
					return res
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'select':
				res = self.handle_select(req)
				if not res == None:
					return res
			elif isinstance(req, receive.REQ_DATA) and req.req_type == 'like':
				res = self.handle_like(req)
				if not res == None:
					return res
			
			print 'NOT HANDLED !'
			return 'success'
		except Exception, Argment:
			return Argment

	def handle_register(self, req):
		print('register:\nusrname: %s\npasswd: %s\nemail: %s\ntel: %s\n'\
			% (req.usr_name, req.passwd, req.email, req.tel))
		res = reply.RES_REGISTER('SUCCESS')
		return res.send()