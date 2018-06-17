import string, random, time

def get_new_info_with_label_sql(base_id = 100, num = 100):
	with open('source/job_info.txt', encoding = 'utf8') as f:
		job_infos = f.readlines()
	job_infos = [e.replace('\n', '') for e in job_infos]
	with open('source/code_term.txt', encoding = 'utf8') as f:
		code_terms = f.readlines()
	code_terms = [e.replace('\n', '') for e in code_terms]

	info_sql = ''
	label_sql = ''
	for i in range(num):
		info_sql += """
		insert into info values(
			{}, '{}', {}, {}, '{}', '{}', '{}', '{}',
			'{}', '{}', '{}', '{}', '{}', '{}', {}
		);""".format(
			base_id + i, # info_id
			('开发', '测试', '运维', '设计')[random.randint(0, 3)], # job_name
			random.randint(6000, 8000), # job_salary
			random.randint(1, 10), # job_num
			job_infos[random.randint(0, len(job_infos) - 1)], # job_info
			''.join((code_terms[random.randint(0, len(code_terms) - 1)] for i in range(4))), # job_req
			'', # job_url
			('百度', '网易', '阿里巴巴', '谷歌中国')[random.randint(0, 3)], # company_name
			'', # company_info
			'', # company_url
			time.strftime('%Y-%m-%d %H:%M:%S'), # apply_time
			'1'.join(random.choice(string.digits) for i in range(10)), # apply_tel
			''.join(random.choice(string.hexdigits) for i in range(5)) + # apply_email
				'@{}.com'.format(('qq', 'gmail', '163', 'outlook')[random.randint(0, 3)]),
			time.strftime('%Y-%m-%d'), # attr_time
			random.randint(0, 10) # attr_expire
		)

		# multi label
		for j in range(2):
			label_sql += """
			insert into info_label values(
				{}, '{}'
			);""".format(
				base_id + i, # info_id
				('C/C++', 'Python', 'Dev', 'Software', 'Web', 'Game',
					'Guangzhou')[random.randint(0, 6)] # label
			)

	return info_sql + label_sql

def get_new_usr_with_like_sql(rand_range = (100, 200), num = 100):
	with open('source/name.txt', encoding = 'utf8') as f:
		usr_names = f.readlines()
	usr_names = [e.replace('\n', '') for e in usr_names]
	random.shuffle(usr_names)

	usr_sql = ''
	like_sql = ''
	for i in range(num):
		usr_name = ''.join(random.choice(string.hexdigits) for i in range(5))
		
		usr_sql += """
		insert into usr values(
			'{}', '{}', '{}', '{}', '{}'
		);""".format(
			usr_name, # usr_name
			''.join(random.choice(string.hexdigits) for i in range(8)), # passwd
			usr_names[i], # wx_id
			''.join(random.choice(string.hexdigits) for i in range(5)) + # email
				'@{}.com'.format(('qq', 'gmail', '163', 'outlook')[random.randint(0, 3)]),
			'1'.join(random.choice(string.digits) for i in range(10))
		)

		for i in range(4):
			if random.random() > 0.5:
				like_sql += """
				insert into usr_like values(
					'{}', {}
				);""".format(
					usr_name,
					random.randint(rand_range[0], rand_range[1]) # info_id
				)

	return usr_sql + like_sql

if __name__ == '__main__':
	with open('add_test_data.sql', 'w') as f:
		f.write(get_new_info_with_label_sql())
		f.write(get_new_usr_with_like_sql())