-- 创建人力资源管理系统数据库
drop database if exists HRS;
create database HRS default charset utf8;
-- 切换数据库上下文环境
use HRS;
-- 删除表
drop table if exists TbEmp;
drop table if exists TbDept;
-- 创建部门表
create table TbDept
(
dno int,										-- 部门编号
dname varchar(10) not null,	-- 部门名称
dloc varchar(20) not null,	-- 部门所在地
primary key (dno)
);
-- 添加部门记录
insert into TbDept values 
(10, '会计部', '北京'),
(20, '研发部', '成都'),
(30, '销售部', '重庆'),
(40, '运维部', '深圳');
-- 创建员工表
create table TbEmp
(
empno int primary key,			-- 员工编号
ename varchar(20) not null,	-- 员工姓名
job varchar(20) not null,		-- 员工职位
mgr int,										-- 主管编号
sal int not null,						-- 员工月薪
comm int,										-- 每月补贴
dno int not null						-- 部门编号
);
-- 添加外键约束
alter table TbEmp add constraint fk_emp_dno foreign key (dno) references TbDept(dno);
-- 添加员工记录
insert low_priority into TbEmp values 
(7800, '张三丰', '总裁', null, 9000, 1200, 20),
(2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
(3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
(3211, '张无忌', '程序员', 2056, 3200, null, 20),
(3233, '丘处机', '程序员', 2056, 3400, null, 20),
(3251, '张翠山', '程序员', 2056, 4000, null, 20),
(5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
(5234, '郭靖', '出纳', 5566, 2000, null, 10),
(3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
(1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
(4466, '苗人凤', '销售员', 3344, 2500, null, 30),
(3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
(3577, '杨过', '会计', 5566, 2200, null, 10),
(3588, '朱九真', '会计', 5566, 2500, null, 10);

use hrs;
-- 查询薪资最高的员工姓名和工资
select ename, (sal+ifnull(comm, 0)) from TbEmp where (sal+ifnull(comm, 0))=(select max(sal+ifnull(comm, 0)) from TbEmp);
select ename, sal from TbEmp where sal=(select max(sal) from TbEmp);
select ename,sal from TbEmp where sal>= all (select sal from TbEmp);

-- 查询员工的姓名和年薪((月薪+补贴)*13)
select ename, (sal+ifnull(comm, 0))*13 from TbEmp;

-- 查询有员工的部门的编号和人数
select t1.dno,t1.dname,t2.counter from TbDept t1 
right outer join (select dno,count(*) as counter from TbEmp group by dno) t2 
on t1.dno=t2.dno; 

-- 查询所有部门的名称和人数
select t1.dno,t1.dname,ifnull(t2.counter,0) from TbDept t1 
left outer join (select dno,count(*) as counter from TbEmp group by dno) t2 
on t1.dno=t2.dno; 

-- 查询除老板外薪资最高的员工的姓名和工资
select ename, (sal+ifnull(comm, 0)) from TbEmp 
where (sal+ifnull(comm, 0))=(select max(sal+ifnull(comm, 0)) from TbEmp where mgr is not null);

-- 查询薪水超过平均薪水的员工的姓名和工资
select ename, sal from TbEmp where sal>(select avg(sal) from TbEmp);

-- 查询薪水超过其所在部门平均薪水的员工的姓名、部门编号和工资
select t1.ename,t1.sal,t1.dno,t2.avgs from TbEmp t1,
(select dno,avg(sal) as avgs from TbEmp group by dno) t2
where t1.dno=t2.dno
and t1.sal>t2.avgs;

-- 查询部门中薪水最高的人姓名、工资和所在部门名称
select t1.dno, t3.dname, t1.ename, t1.sal from TbEmp t1, TbDept t3,(select dno,max(sal) as msal from TbEmp group by dno) t2
where t1.sal=t2.msal and t1.dno=t2.dno and t1.dno=t3.dno;

-- 查询主管的姓名和职位
-- 使用distinct和in集合运算，这种方式效率极低
select ename,job from tbEmp where empno in (select DISTINCT mgr from TbEmp where mgr is not null);
-- 可使用exists、not exists方式代替
select empno,ename,job from tbEmp t1 where exists(select mgr from tbEmp t2 where t1.mgr=t2.empno);

-- 查询薪资排名4~6名的员工姓名和工资
select ename,(sal+ifnull(comm,0)) as msal from TbEmp order by msal desc limit 3,3;
