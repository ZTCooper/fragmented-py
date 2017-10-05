* `os.urandom(n)`随机产生n字节的字符串，可作为随机加密 key  
```python
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
```  
![](imgs/os.jpg)