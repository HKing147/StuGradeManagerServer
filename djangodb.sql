drop database if exists djangodb;
create database djangodb;
use djangodb;
 
create table college(
cid int auto_increment primary key,
cname varchar(20),
ccharge varchar(20)
);

create table department(
did int auto_increment primary key,
dname varchar(20),
dcharge varchar(20),
cid int,
foreign key(cid) references college(cid) on delete cascade
);

create table jiaoyan(
jid int auto_increment primary key,
jname varchar(20),
jcharge varchar(20),
did int,
foreign key(did) references department(did) on delete cascade
);

create table class(
cid int auto_increment primary key,
cname varchar(20),
did int,
foreign key(did) references department(did) on delete cascade
);

create table teacher(
tid int auto_increment primary key,
tname varchar(20),
trank int,
jid int,
foreign key(jid) references jiaoyan(jid) on delete cascade
);

create table student(
sid int auto_increment primary key,
sname varchar(20),
ssex int,
cid int,
foreign key(cid) references class(cid) on delete cascade
);

create table course(
cid int auto_increment primary key,
cname varchar(20)
);

create table stugrades(
sid int,
cid int,
sgrade int,
foreign key(cid) references course(cid) on delete cascade
);

create table Teacher_Class_Course(
tid int,
claid int,
couid int,
foreign key(claid) references class(cid) on delete cascade,
foreign key(couid) references course(cid) on delete cascade
);

