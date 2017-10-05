### 10.05.2017  

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