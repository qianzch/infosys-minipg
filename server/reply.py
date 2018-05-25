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
	def __init__(self, err_info, infos):
		self.__dict = dict()
		self.__dict['ErrInfo'] = err_info
		self.infos = infos

	def __get_label(self, label):
		xml = """
		<Label><![CDATA[{}]]></Label>
		""".format(label)
		return xml

	def __get_piece(self, info):
		labels = ''
		for e in info.labels:
			labels += self.__get_label(e)
		xml = """
		<Piece>
			<Id><![CDATA[{info.info_id}]]></Id>
			<Job>
				<Name><![CDATA[{info.job_name}]]></Name>
				<Salary><![CDATA[{info.job_salary}]]></Salary>
				<Number><![CDATA[{info.job_num}]]></Number>
				<Info><![CDATA[{info.job_info}]]></Info>
				<Req><![CDATA[{info.job_req}]]></Req>
				<Url><![CDATA[{info.job_url}]]></Url>
			</Job>
			<Company>
				<Name><![CDATA[{info.company_name}]]></Name>
				<Info><![CDATA[{info.company_info}]]></Info>
				<Url><![CDATA[{info.company_url}]]></Url>
			</Company>
			<Apply>
				<InterviewTime><![CDATA[{info.apply_time}]]></InterviewTime>
				<Tel><![CDATA[{info.apply_tel}]]></Tel>
				<Email><![CDATA[{info.apply_email}]]></Email>
			</Apply>
			<Attr>
				<Labels>
					{labels}
				</Labels>
				<Time><![CDATA[{info.attr_time}]]></Time>
				<Expire><![CDATA[{info.attr_expire}]]></Expire>
			</Attr>
		</Piece>
		""".format(info = info, labels = labels)
		return xml

	def send(self):
		XmlForm = """
		<xml>
		<ErrInfo><![CDATA[{ErrInfo}]]></ErrInfo>
		""".format(**self.__dict)
		for e in self.infos:
			XmlForm += self.__get_piece(e)
		XmlForm += '</xml>'
		return XmlForm

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