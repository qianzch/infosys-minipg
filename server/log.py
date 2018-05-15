class REQ_TYPE():
	register 	= 1
	login 		= 2
	select 		= 3
	like 		= 4

class LOG():
	@staticmethod
	def logi(data, req_type):
		info = 'logi: none'
		if req_type == REQ_TYPE.register:
			info = """
			register:
			user name: {data.usr_name}
			passwd: {data.passwd}
			email: {data.email}
			tel: {data.tel}
			""".format(data = data)
		elif req_type == REQ_TYPE.login:
			info = """
			login:
			user name: {data.usr_name}
			passwd: {data.passwd}
			""".format(data = data)
		elif req_type == REQ_TYPE.select:
			info = """
			select:
			IDs: {data.ids}
			labels: {data.labels}
			keywords: {data.keywords}
			method: {data.method}
			""".format(data = data)
		elif req_type == REQ_TYPE.like:
			info = """
			like:
			user name: {data.usr_name}
			ID: {data.id}
			get noti: {data.get_noti}
			""".format(data = data)
		print info