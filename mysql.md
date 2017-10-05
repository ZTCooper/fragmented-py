### 10.05.2017  

* 库的操作：  
```
mysql> create database test;
mysql> show database;
mysql> use database;
mysql> drop database test;
```  
  
* 表的操作：  
```
mysql> create table people(
    -> num int,
    -> name varchar(20),
    -> loc varchar(40)
    -> );

mysql> describe people;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| num   | int(11)     | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
| loc   | varchar(40) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

mysql> alter table people add descri varchar(20);
mysql> alter table people modify num varchar(20);
mysql> alter table people change loc location varchar(40);
mysql> alter table people modify name varchar(20) after location;

mysql> describe people;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| num      | varchar(20) | YES  |     | NULL    |       |
| location | varchar(40) | YES  |     | NULL    |       |
| name     | varchar(20) | YES  |     | NULL    |       |
| descri   | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
mysql> alter table people drop descri;
```  
  
* 数据的操作：  
```
mysql> insert into people(num, location, name)
    -> values(1, 'wuxi', 'zt');

mysql> insert into people
    -> values(2, 'nanjing','zyp'),
    -> (3, 'beijing','qjw');

mysql> update people
    -> set location ='lanzhou'
    -> where name = 'qjw';

mysql> delete from people
    -> where name = 'zyp';

mysql> select * from people;
+------+----------+------+
| num  | location | name |
+------+----------+------+
| 1    | wuxi     | zt   |
| 3    | lanzhou  | qjw  |
+------+----------+------+
```  
  
* 数据查询：  
```
mysql> select name from people
    -> where location='wuxi';
+------+
| name |
+------+
| zt   |
+------+

mysql> select name from people
    -> where num between 2 and 3;
+------+
| name |
+------+
| qjw  |
+------+
```  
  
* pymysql 
```
>>> import pymysql
>>> conn = pymysql.connect(host='127.0.0.1',port=3306,user='zt',password='xxx')
	#创建连接
>>> cursor = conn.cursor()
	#创建游标
```