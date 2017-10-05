
>>> import re
>>> re.search(r'Python', 'I love Python.com')
<_sre.SRE_Match object; span=(7, 13), match='Python'>
>>> #search()在字符串中搜索第一次匹配的位置
>>>
>>> re.search(r'.', 'I love Python')
<_sre.SRE_Match object; span=(0, 1), match='I'>
>>> re.search(r'Py.', 'I love Python')
<_sre.SRE_Match object; span=(7, 10), match='Pyt'>
>>> # . 通配符，可匹配除 \n 外的所有字符
>>>
>>> re.search(r'\.', 'I love Python.com')
<_sre.SRE_Match object; span=(13, 14), match='.'>
>>> # \ 消除特殊功能
>>> re.search(r'\d', 'I love Python123.com')
<_sre.SRE_Match object; span=(13, 14), match='1'>
>>> re.search(r'\d\d\d', 'I love Python123.com')
<_sre.SRE_Match object; span=(13, 16), match='123'>
>>> # \d 匹配数字
>>> re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', '102.168.111.123')
<_sre.SRE_Match object; span=(0, 15), match='102.168.111.123'>
>>> #匹配IP成功
>>> #But \d\d\d 最大匹配999，而IP地址不超255
>>> #IP地址后面部分不确定
>>>
>>> re.search(r'[aeiou]', 'I love Python')
<_sre.SRE_Match object; span=(3, 4), match='o'>
>>> # [] 创建字符类，可匹配字符类中任意字符
>>> #大小写敏感模式
>>> re.search(r'[a-z]', 'I love Python')
<_sre.SRE_Match object; span=(2, 3), match='l'>
>>> re.search(r'[0-9]', 'I love Python123.com')
<_sre.SRE_Match object; span=(13, 14), match='1'>
>>> # [ - ] 可表示范围
>>>
>>> re.search(r'ab{3}c', 'abbbc')
<_sre.SRE_Match object; span=(0, 5), match='abbbc'>
>>> re.search(r'ab{3}c', 'abbbbc')
>>> # {} 重复匹配次数
>>> re.search(r'ab{3,10}c', 'abbbbbbbc')
<_sre.SRE_Match object; span=(0, 9), match='abbbbbbbc'>
>>> # {a,b} 重复次数范围
>>>
>>> re.search(r'[01]\d\d|2[0-4]\d|25[0-5]', '188')
<_sre.SRE_Match object; span=(0, 3), match='188'>
>>> #匹配 0-255
>>> re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])', '192.168.111.123')
<_sre.SRE_Match object; span=(0, 15), match='192.168.111.123'>
>>> re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.){3}([01]\d\d|2[0-4]\d|25[0-5])', '192.168.1.1')
>>> #匹配失败
>>> # () 分组，()中整个部分匹配3次
>>> re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', '192.168.1.1')
<_sre.SRE_Match object; span=(0, 11), match='192.168.1.1'>
>>> #有bug
>>>
>>> re.search(r'Python(2|3)', 'I love Python3')
<_sre.SRE_Match object; span=(7, 14), match='Python3'>
>>> re.search(r'Python(2|3)', 'I love Python2')
<_sre.SRE_Match object; span=(7, 14), match='Python2'>
>>> # | 管道符，或
>>>
>>> re.search(r'^Python', 'I love Python')
>>> re.search(r'^Python', 'Python love me')
<_sre.SRE_Match object; span=(0, 6), match='Python'>
>>> # ^脱字符，匹配开头位置
>>>
>>> re.search(r'Python$', 'Python love me')
>>> re.search(r'Python$', 'I love Python')
<_sre.SRE_Match object; span=(7, 13), match='Python'>
>>> # $ 匹配结束位置
>>>
>>> re.search(r'(Python)\1', 'I love Python')
>>> re.search(r'(Python)\1', 'I love PythonPython')
<_sre.SRE_Match object; span=(7, 19), match='PythonPython'>
>>> # \ 后数字为1-99，表示引用序号对应的子组所匹配的字符串
>>> re.search(r'(Python)\060', 'I love Python0')
<_sre.SRE_Match object; span=(7, 14), match='Python0'>
>>> re.search(r'(Python)\141', 'Pythona')
<_sre.SRE_Match object; span=(0, 7), match='Pythona'>
>>> # \ 后数字为 八进制， 表示对应的ASCII
>>> # r'(Python)\1 == r'PythonPython'
>>>
>>> re.search(r'.', 'I love Python')
<_sre.SRE_Match object; span=(0, 1), match='I'>
>>> re.search(r'\.', 'I love Python.com')
<_sre.SRE_Match object; span=(13, 14), match='.'>
>>> re.search(r'[.]', 'I love Python.com')
<_sre.SRE_Match object; span=(13, 14), match='.'>
>>> # [] 字符类，[.] == \.
>>> re.findall(r'[a-z]', 'Python.com')
['y', 't', 'h', 'o', 'n', 'c', 'o', 'm']
>>> # findall() 找到所有字符串， 打包为列表返回
>>> # [\] 报错：\ 转义
>>> re.findall(r'^[a-z]', 'Python.com')
[]
>>> re.findall(r'[^a-z]', 'Python.com')
['P', '.']
>>> # ^ 取反， 置于前面
>>> re.findall(r'[a-z^]', 'Python.com^')
['y', 't', 'h', 'o', 'n', 'c', 'o', 'm', '^']
>>> # 若置于后面则表示匹配 '^' 本身
>>>
>>> # {} 匹配多次，{a,b} a-b次
>>> # * 匹配 0次 或 多次， 相当于{0,}
>>> # + 匹配 1次 或 多次， 相当于{1,}
>>> # ? 匹配 0次 或 1次，  相当于{0.1}
>>>
>>> s = "<html><title>I love Python</title></html>"
>>> re.search(r'<.+>', s)
<_sre.SRE_Match object; span=(0, 41), match='<html><title>I love Python</title></html>'>
>>> # 贪婪，条件符合的情况下尽可能多地匹配
>>> re.search(r'<.+?>', s)
<_sre.SRE_Match object; span=(0, 6), match='<html>'>
>>> # 在表示重复的元字符后加 '?' 启用非贪婪模式，遇到第一个匹配则停止
>>>
>>> re.search(r'(.+) \1', '555 555')
<_sre.SRE_Match object; span=(0, 7), match='555 555'>
>>> re.search(r'(.+) \1', 'python python')
<_sre.SRE_Match object; span=(0, 13), match='python python'>
>>>
>>> # 默认情况下
>>> # \A == ^ (如果设置 re.MUITLINE 标志，^也匹配 \n 后的位置)
>>> # \Z == $ (如果设置 re.MUITLINE 标志，^也匹配 \n 前的位置)
>>> # \A \Z 无此性质
>>> re.findall(r'\bPython\b', 'Python.com!Python_com!(Python)')
['Python', 'Python']
>>> # \b 匹配单词边界，第二个'Python_com'不被找到（字母数字下横线）
>>> # \B 匹配非单词边界，py\B 会匹配 'python', 'py2'，不会匹配'py ', 'py.', 'py!'...
>>> # 以上零宽断言（不匹配任何字符，只用于定位）
>>> # \d (digital)
>>> # \D 与 \d 相反，匹配非unicode字符，若开启 re.ASCII，则匹配[^0-9]
>>> # \s 匹配 unicode 中空白字符(包括[\t\n\r\f\v])，若开启 re.ASCII，只匹配[\t\n\r\f\v]
>>> # \S 与 \s 相反
>>> # \w 匹配单词字符，包括'_'
>>> # \W 与 \w 相反
>>>
>>> # \b 通常表示单词边界，只有在[]中表示backspace

