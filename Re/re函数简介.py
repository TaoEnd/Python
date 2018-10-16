# coding:utf-8

import re

r'''
re.match(pattern, string, flags=0)
pattern：匹配的正则表达式
string：需要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式（比如是否忽略大小写）
flags的取值为：
	re.I：忽略大小写
	re.L：做本地用户识别
	re.M：多行匹配，影响 ^ 和 $ 
	re.S：是 . 匹配，包括换行符在内的所有字符
	re.U：根据Unicode字符集解析字符，影响\w、\W、\b、\B
	re.X：使我们以更灵活的格式理解正则表达式
'''
print(re.match("www", "www.baidu.com"))
print(re.match("www", "wwW.baidu.com", flags=re.I))
print('------------------')

'''
re.search(pattern, string, flags=0)
'''
print(re.search("man", "he is a good man, she is a woman"))
print('------------------')

'''
re.findall(pattern, string, flags)
'''
print(re.findall("man", "he is a good man, she is a woman"))
