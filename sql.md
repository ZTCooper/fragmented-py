* [mysql](#1)
* [pymysql](#2)

<a id = '1'></a>
* mysql库的操作：  
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
```
* [alter命令](https://www.w3cschool.cn/mysql/mysql-alter.html)
```
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
    
insert ignore into 避免插入重复数据

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

like字句
mysql> SELECT * from w3cschool_tbl 
    -> WHERE w3cschool_author LIKE '%jay'

mysql> select name from people
    -> where num between 2 and 3;
+------+
| name |
+------+
| qjw  |
+------+

binary设定大小写敏感
mysql> SELECT * from w3cschool_tbl \
          WHERE BINARY w3cschool_author='sanjay';
	  
	  
oeder by排序
升序
mysql> SELECT * from w3cschool_tbl ORDER BY w3cschool_author ASC;
降序
mysql> SELECT * from w3cschool_tbl ORDER BY w3cschool_author DESC;


group by
with rollup
coalesce 来设置一个可以取代 NUll 的名称
mysql> SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------------------------+--------------+
| coalesce(name, '总数') | singin_count |
+--------------------------+--------------+
| 小丽                   |            2 |
| 小明                   |            7 |
| 小王                   |            7 |
| 总数                   |           16 |
+--------------------------+--------------+

group by 获取不重复数据
mysql> SELECT last_name, first_name
    -> FROM person_tbl
    -> GROUP BY (last_name, first_name);

distinct 过滤重复
mysql> SELECT DISTINCT last_name, first_name
    -> FROM person_tbl
    -> ORDER BY last_name;

update修改数据表数据
mysql> UPDATE w3cschool_tbl 
    -> SET w3cschool_title='Learning JAVA' 
    -> WHERE w3cschool_id=3
```  
* 正则表达式
```
mysql> SELECT name FROM person_tbl WHERE name REGEXP '^st';
```
  
  
<a id = '2'></a>
* pymysql 
```
>>> import pymysql
>>> conn = pymysql.connect(host='127.0.0.1',port=3306,user='zt',password='xxx',db='test')
	#创建连接
>>> cur = conn.cursor()
	#创建游标
```  

1. 插入数据
```python
ret = cur.excute('insert into table(field1, field2) values(%s,%s)', (a,b))
#插入一条数据
ret = cur.excutemany('insert into table(f1, f2) values(%s,%s)',[(a1,b1),(a2,b2)])
#插入多条数据
conn.commit()   #提交
cur.close()     #关闭指针对象
conn.close()    #关闭连接对象
```
2. 查询数据  
`cur.fetchall()` `cur.fetchone` `cur.fetchmany(3)`
```python
cur.execute('select * from table')
#查询表中存在数据
```  
`cursor.scroll(num, mode)`移动游标位置  
```python
cursor.scroll(1,mode='relative')  
#相对当前位置移动【1：表示向下移动一行，-1：表示向上移动一行】
cursor.scroll(2,mode='absolute') 
#相对绝对位置移动
```
3. 删除数据  
`cur.execute("delete * from lcj")`
4. 修改数据  
`cur.execute('UPDATE table set f1 = 'new' where f1='old')`
5. fetch数据类型  
`cur = conn.cursor(cursor=pymysql.cursors.DictCursor)`
```python
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#游标设置为字典类型
cur.excute(select * from table)
ret = cur.fetchall()
```
