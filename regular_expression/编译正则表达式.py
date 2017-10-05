>>> # 编译正则表达式
>>> # 如果需要重复使用某个正则表达式，则可以先将该正则表达式编译成模式对象
>>> # 使用 re.compile() 方法来编译
>>>
>>> p = re.compile(r'[A-Z]')    #将模式对象赋值给p
>>> type(p)
<class '_sre.SRE_Pattern'>
>>> p.search('I love Python')
<_sre.SRE_Match object; span=(0, 1), match='I'>
>>> p.findall('I love Python')
['I', 'P']
>>>
>>> # 效率相似，若只使用一次，则选用模块级别，若循环多次则先编译
>>>
>>> #编译标志
>>> # 编译标志：完整名和简写
>>> # ASCII    A    转义符号 \w\b\s\d 只能匹配ASCII字符
>>> # DOTALL    S    使得 . 匹配任何符号，包括换行符
>>> # IGNORECASE   I    不区分大小写
>>> # LOCALE    L    支持当前语言区域设置
>>> # MULTILINE    M    多行匹配，影响 ^ 和 $
>>> # VERBOSE    X(extended)    启用详细的正则表达式
>>>
>>>
>>> # search()返回匹配对象
>>> result = re.search(r' (\w+) (\w+)', 'I love Python.com')
>>> result
<_sre.SRE_Match object; span=(1, 13), match=' love Python'>
>>> result.group()
' love Python'
>>> result.group(1)
'love'
>>> result.group(2)
'Python'
>>> # 返回子组中对应序号的字符串
>>> result.start()
1
>>> result.end()
13
>>> result.span()
(1, 13)
>>>
>>> #findall()返回匹配字符串列表
>>> # findall()返回匹配字符串列表
>>> # 若给出的正则表达式中包含子组，则单独返回子组内容，若存在多个子组，则见子组组合为元组返回
>>> # (?...) 为正则表达式的扩展语法
>>> # (?:)    非捕获组 即该子组匹配的字符串无法从后边获取
