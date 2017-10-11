### 10.07.2017  
* `os.urandom(n)`随机产生n字节的字符串，可作为随机加密 key  
```python
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
```  
[os和os.path](https://github.com/ZTCooper/fragmented_py/blob/master/imgs/os.jpg)  

### 10.09.2017  
```python
with open(file_name, encoding = 'gbk', errors='ignore') as f:
	if os.path.isdir(file):        #判断路径存在且是一个目录
		search_file(file)
		os.chdir(os.pardir)				#返回上一级操作目录

#或者直接os.walk(start_dir)
#返回(root,dirs,files)
```   

```python
try:
	... ...
except UnicodeDecodeError:
	pass    #忽略格式不兼容的文件
```

### 10.06.2017  
* pillow  
```python
from PIL import Image
im = Image.open('0.jpg')

from __future__ import print_function
print(im.format, im.size, im.mode)
# JPEG (1080, 1080) RGB

im.show()
```  
创建缩略图`im.thumbnail(size)`  
[etc.](http://python.jobbole.com/83685/)  

* UUID  
```python
import uuid
key = str(uuid.uuid4())
```
[生成随机激活码](https://github.com/ZTCooper/show-me-the-code/tree/master/ztcooper/0001)  
  
* [string](https://github.com/ZTCooper/fragmented_py/blob/master/string.md)  
  
### 10.11.2017
```python
'sep'.join(sep)
os.path.join(path1,[,path2,[,...]])
```