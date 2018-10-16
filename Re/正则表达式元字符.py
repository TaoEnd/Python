# coding:utf-8

import re

# 匹配单个字符与数据
r'''
. ：            匹配除换行符以外的任意字符
[0123456789]：  表示匹配[ ]内任意一个字符
[a-z]：         匹配任意小写字母
[0-9a-zA-Z]：   匹配 0-9 和所有大小写字母
[^nice]：       匹配除了nice这几个字符以外的所有字符
'''
print(re.search(".", "he is a good man"))
print(re.search("[123456]", "his phone is 123"))
print(re.search("[nice]", "his phone is 123"))
print(re.search("[0-9a-zA-Z]", "he is good man"))
print(re.search("[^nice]", "his phone is 123"))
