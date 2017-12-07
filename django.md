
* *django 1.9* 后 `python manage.py syncdb` 已不适用  
创建 app 定义 class 后，加入到 **INSTALLED_APPS** 中， 执行以下命令 creat table  
```
python manage.py makemigrations
python manage.py migrate
``` 
创建 superuser:  
```
python manage.py createsuperuser
```  
  

* 存储到 database 的时间比本地早8小时   
修改 **settings.py**   
```python
USE_TZ = True
TIME_ZONE = 'Asia/Shanghai'
```  
  
* mysqldb 不支持 python3.6  
改用 pymysql，修改站点 **\_\_init\_\_.py**  
```python
import pymysql
pymysql.install_as_MySQLdb()
```

* ModelAdmin也要register才行

* {% csrf_token %} views中要用render才可以

* 注意url的正则表达式！天呐！找了一晚上bug！（傻了我……

* DateTimeField(auto_now = True)

* DEBUG = False 时需添加 ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
