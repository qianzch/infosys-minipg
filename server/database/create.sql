create user 'infosys_dev'@'%' identified by 'softwareengineering';
create database infosys_minipg;
use infosys_minipg;
grant insert, delete, select, update on infosys_minipg.* to 'infosys_dev'@'%';

create table usr(
	usr_name	varchar(32)	not null primary key,
    passwd		varchar(32) not null,
    wx_id		varchar(32),
    email		varchar(32),
    tel			varchar(32)
);

create table info(
	info_id			int(8)		not null primary key auto_increment,
    job_name		varchar(32)	not null,
    job_salary		int(8),
    job_num			int(8),
    job_info		varchar(256),
    job_req			varchar(128),
    job_url			varchar(128),
    company_name	varchar(32),
    company_info	varchar(256),
    company_url		varchar(128),
    apply_time		datetime,
    apply_tel		varchar(32),
    apply_email		varchar(32),
    attr_time		date,
    attr_expire		int(8)
);

create table info_label(
	info_id		int(8) 		not null references info(info_id),
    label		varchar(32)	not null
);

create table usr_like(
	usr_name	varchar(32)	not null references usr(usr_name),
    info_id		int(8)		not null references info(info_id)
);