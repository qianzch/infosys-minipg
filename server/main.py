# -*- coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8') 
import web
from handle import Handle

urls = (
	'/', 'Handle',
)

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()