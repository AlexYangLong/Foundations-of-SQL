create table tb_user
(
username varchar(20) not null,
userpass varchar(20) not null,
primary key (username)
);

insert into tb_user values ('admin', '1qaz2wsx');


create table tb_account
(
accid char(4) not null,
uname varchar(20) not null,
balance float default 0,
primary key (accid)
);

insert into tb_account values 
('1111', '骆昊', 1200.0),
('1122', '王大锤', 500);

-- 事务
begin;
update tb_account set balance=balance-100 where accid='1111';
update tb_account set balance=balance+100 where accid='1122';
commit;
rollback;

begin;
delete from tbemp;
rollback;
