|大小写：| |
|---|---|
|s.capitalize()|把字符串的第一个字符改为大写；|
|s.casefold	()|把整个字符串的所有字符改为小写；|
|s.lower()|所有大写字符转小写；|
|s.upper()|所有小写字符转大写；|
|s.swapcase()|翻转字符串中大小写；|
|s.title()|返回标题化（所有单词大写开始）；|
|格式：||
|s.strip([chars])|删除前后空格，chars定制删除字符；|
|s.lstrip()|去掉字符串左边所有空格；|
|s.rstrip|删除字符串末尾空格；|
|s.ljust(width)|返回一个左对齐的字符串，并使用空格填充至长度为width；|
|s.rjust(width)|返回一个右对齐的字符串，并使用空格填充至长度为width；|
|s.zfill(width)|返回长度为width的字符串，原字符串右对齐，前边用0填充。|
|s.center(width)|将字符串居中，使用空格填充至width长度；|
|s.expandtabs([tabsize=8])|把字符串中的tab符号(\t)转换为空格，默认tabsize=8；|
|s.encode(encoding=’utf-8’, errors=’strict’)|以encoding指定的编码格式对字符串进行编码；|
内容：
|s.count(sub[,start[,end]])|返回sun在字符串里出现的次数，start和end表范围；|
|s.endswith(sub[,start[,end]])|检测字符串是否以sub子字符串结尾；|
|s.startswith(prefix[,start[,end]])|检测字符串是否以prefix子字符串开头；|
|s.find(sub[,start[,end]])|	检测sub是否包含在字符串中，有则返回索引值，否则返回-1；|
|s.rfind(sub[,start[,end]])|从右边开始查找；|
|s.index(sub[,start[,end]])|与find相同，不存在则产生异常；|
|s.rindex(sub[,start[,end]])|从右边开始；|
|s.isalnum()|所有字符都是数字或者字母，为真返回 True，否则返回 False；|
|s.isnumeric()|只包含数字字符，为真返回 True，否则返回 False；|
|s.isalpha()|所有字符都是字母，为真返回 True，否则返回 False；|
|s.isdigit()|所有字符都是数字，为真返回 True，否则返回 False；|
|s.islower()|所有字符都是小写，为真返回 True，否则返回 False；|
|s.isupper()|所有字符都是大写，为真返回 True，否则返回 False；|
|s.istitle()|所有单词都是首字母大写，为真返回 True，否则返回 False；|
|s.isspace()|所有字符都是空白字符，为真返回 True，否则返回 False；|
|s.isdecimal()|字符串只包含十进制数字则返回 True，否则返回 False；|
|s.isspace()|只包含空格，为真返回 True，否则返回 False；|
|s.join(sub)|以s为分隔符，插入到sub中所有字符之间；|
|s.partition(sub)|找到字符串sub，把字符串分成一个3元组(pre_sub,sub,fol_sub)，如果字符串中不包含sub则返回(‘原字符串’,”,”)|
|s.rpartition(sub)|右边开始查找；|
|s.replace(old, new[, count])|new替换old，替换不超过count次；|
|s.split(sep=None, maxsplit=-1)|按照空格切割为列表，带参数则按照参数切割；|
|s.splitlines(([keepends]])|按照’\n’切割|
|s.translate(table)|根据table的规则（可以由str.maketrans(‘a’,’b’)定制）转化字符串中的字符：（s.translate(str.maketrans(‘b’, ‘a’)将字符串中所有a 转换为b）|
|s.count(each)|