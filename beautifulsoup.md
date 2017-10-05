# BeautifulSoup<br>
[Beautiful Soup 4.4.0 documentation 
](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)  
*** 
  
主要在爬虫中写parse用到   
完整的**Scrapy project**在这里：  
[**个人爬虫集：carwler_scrapy**](https://github.com/ZTCooper/crawler_scrapy)   
  

## 目录
* [准备工作](#1)  
	* 安装	
	*  导入	
	* 实例化
* [开始使用](#2)
	* [四大对象种类](#2.1)
		* Tag
		* NavigatbleString
		* BeautifulSoup
		* Comment
	* [遍历文档树](#2.2)
		* 直接子节点
		* 所有孙子节点
		* 节点内容
		* 多个内容
		* 父节点
		* 全部父节点
		* 兄弟节点
		* 全部兄弟节点
		* 前后节点
		* 所有前后节点
	* [搜索文档树](#2.3)
	* **[CSS选择器](#2.4)**
		* 通过标签名查找
		* 通过类名查找
		* 通过 id 名查找
		* 组合查找
		* 属性查找  
* [示例html文件](https://github.com/ZTCooper/fragmented_py/blob/master/example.html)

***
### <a id="1"></a>一、准备工作：
1.  **安装：**  <br>
`conda install bs4`
2.  **导入beautifulsoup4：**<br>
`from bs4 import BeautifulSoup`
3.  **实例化对象：**<br>
`soup = BeautifulSoup(html)`  <br>
或者 用本地 HTML 文件来创建对象：<br>
`soup = BeautifulSoup(open('xxx.html'))`<br>
4.  soup 对象内容格式化：<br>
`soup.prettify()`<br>
  
### <a id="2"></a>二、开始使用 ：
#### <a id="2.1"></a>（一）四大对象种类
1.  **Tag 标签：**   

获取**Tag**（只查找到第一个位置）：
```Python
print soup.title
#<title>The Dormouse's story</title>

soup.head
soup.a
......
```
  **Tag** 的两个属性：**name** 和 **attr**
```Python
soup.p
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>

print soup.p.attrs
#{'class': ['title'], 'name': 'dromouse'}

print soup.p['class']
#['title']

print soup.p.get('name')
#['dromouse']
```
可对属性内容进行修改或删除：
```Python
soup.p['class']="newClass"
print soup.p
#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

del soup.p['class']
print soup.p
#<p name="dromouse"><b>The Dormouse's story</b></p>
```
2.  **NavigatbleString**    

获取标签内部文字（`.string`）
```Python
print soup.p.string
#The Dormouse's story
```
3.  **BeautifulSoup**    

表示一个文档的全部内容
```Python
print type(soup.name)
#<type 'unicode'>
print soup.name 
# [document]
print soup.attrs 
#{} 空字典
```
4.  **Comment（特殊类型的 NavigableString 对象）**

使用前判断类型是否为 Comment，避免获取到注释内容：
```Python
if type(soup.a.string)==bs4.element.Comment:
    print soup.a.string
```  
  
    
    
#### <a id="2.2"></a>（二）遍历文档树  

1.  **直接子节点**

**tag** 的 ` .content`  属性可以将 **tag** 的子节点以**列表**的方式输出
由于输出方式为列表，我们可以用列表**索引**来获取它的某一个元素
```Python
print soup.head.contents[0]
#<title>The Dormouse's story</title>
```
`.children`
它返回的**不是**一个 list，是一个 **list 生成器对象**，我们可以通过**遍历**获取所有子节点
```Python
for child in soup.body.children:
    print child
```
2.  **所有孙子节点**

`.descendants`
`.contents` 和` .children` 属性仅包含 **tag** 的直接子节点，`.descendants` 属性可以对所有 **tag** 的子孙节点进行递归循环，和`.children`类似，我们也需要**遍历**获取其中的内容。
```Python
for child in soup.descendants:
    print child
```
3.  **节点内容**

`.string`

4.  **多个内容**

`.strings`
```Python
for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
```
``.stripped_strings``（去除多余空格）
```Python
for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
```

5.  **父节点**

`.parent`
```Python
p = soup.p
print p.parent.name
#body

content = soup.head.title.string
print content.parent.name
#title
```
6.  **全部父节点**

`.parents`
```Python
content = soup.head.title.string
for parent in  content.parents:
    print parent.name

#title
#head
#html
#[document]
```
7.  **兄弟节点**

`.next_sibling`  
`.previous_sibling`

8.  **全部兄弟节点**

`.next_siblings`    
` .previous_siblings`
```Python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
    # u',\n'
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    # u' and\n'
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
    # u'; and they lived at the bottom of a well.'
    # None
```
9.  **前后节点**

`.next_element`
`.previous_element`

不针对兄弟节点，所有节点，不分层次

10.  **所有前后节点**

`.next_elements`   
` .previous_elements`
```Python
for element in last_a_tag.next_elements:
    print(repr(element))
# u'Tillie'
# u';\nand they lived at the bottom of a well.'
# u'\n\n'
# <p class="story">...</p>
# u'...'
# u'\n'
# None
```
  
#### <a id="2.3"></a>（三）搜索文档树  
1.  **find_all()**  
**find_all( name , attrs , recursive , text , \*\*kwargs )**  
**find_all()** 方法搜索当前 **tag** 的所有 **tag** 子节点，并判断是否符合过滤器的条件  


| 参数 | 说明 |
| --- | ---|
| name | 可以查找所有名字为 *name* 的 tag，字符串对象会被自动忽略掉可传入 \[字符串， 正则表达式， 列表， True， 方法\]<br>`soup.find_all('b')`|
| keyword | `soup.find_all(id='link2')` <br> `soup.find_all("a", class_="sister")`<br>`soup.find_all(href=re.compile("elsie"), id='link1')`|
| text | 可传入 \[字符串， 正则表达式， 列表， True， 方法\]<br>`soup.find_all(text="Elsie")`<br>`soup.find_all(text=["Tillie", "Elsie", "Lacie"])`<br>`soup.find_all(text=re.compile("Dormouse"))`|
| limit | 限制返回结果的数量<br>`soup.find_all("a", limit=2)`|
| recursive | 如果只想搜索 **tag** 的直接子节点,可以使用参数 `recursive=False` <br>`soup.html.find_all("title", recursive=False)`|

          
	  

2.  **find( name , attrs , recursive , text , \*\*kwargs)**  <br>
参数用法与 **find_all()** 相同，原理类似  

| 全部 | 一个 |
| --- | ---|
| **find_parents()** |  **find_parent()**|
| **find_next_siblings()** |  **find_next_sibling()**|
| **find_previous_siblings()** |  **find_previous_sibling()**|
| **find_all_next()**  | **find_next()**|
| **find_all_previous()**  | **find_previous()**|
  
    
    
#### <a id="2.4"></a>（四）CSS选择器

用到的方法是`soup.select()`，返回类型是 **list**
**标签名不加任何修饰，类名前加点，id名前加 #**

1.  通过**标签名**查找：
```Python
print soup.select('title')
#[<title>The Dormouse's story</title>]

print soup.select('a')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print soup.select('b')
#[<b>The Dormouse's story</b>]
```
2.  通过**类名**查找：
```Python
print soup.select('.sister')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```
3.  通过**id 名**查找：
```Python
print soup.select('#link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
4.  **组合查找：**
```Python
print soup.select('p #link1')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
直接**子标签**查找：
```Python
print soup.select("head > title")
#[<title>The Dormouse's story</title>]
```
直接**兄弟**标签查找：
```Python
print soup.select('p.story + a').get(href)
#http://example.com/elsie
```
5.  **属性查找：**

属性和标签属于同一节点，中间不加空格，不在同一节点用空格隔开
```Python
print soup.select('a[class="sister"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print soup.select('a[href="http://example.com/elsie"]')
#[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
```
返回 **list** ，可以遍历形式输出，然后用 `.get_text()`方法来获取它的内容：  
```Python
soup = BeautifulSoup(html, 'lxml')
print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
    print title.get_text()
```
在[这里](https://github.com/ZTCooper/crawler_scrapy/blob/master/dmoz/dmoz/spiders/dmoz_spider.py)还有`.get('href')`方法  



