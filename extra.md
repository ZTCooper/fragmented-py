### 10.07.2017  
* `os.urandom(n)`随机产生n字节的字符串，可作为随机加密 key  
```python
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))
```  
[os和os.path](https://github.com/ZTCooper/fragmented_py/blob/master/imgs/os.jpg)  

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
* [string](https://github.com/ZTCooper/fragmented_py/blob/master/string.md)