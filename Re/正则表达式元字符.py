# coding:utf-8

import re

# 匹配单个字符与数据
r'''
. ：            匹配除换行符以外的任意字符
[0123456789]：  表示匹配[ ]内任意一个字符
[a-z]：         匹配任意小写字母
[0-9a-zA-Z]：   匹配 0-9 和所有大小写字母
[^nice]：       匹配除了nice这几个字符以外的所有字符
\d：            匹配所有数字
\D：            匹配所有非数字
'''
print(re.search(".", "he is a good man"))
print(re.search("[123456]", "his phone is 123"))
print(re.search("[nice]", "his phone is 123"))
print(re.search("[0-9a-zA-Z]", "he is good man"))
print(re.search("[^nice]", "his phone is 123"))
print(re.search("\d", "his phone is 123"))

print('----------------------')

# 锚字符（边界字符）
r'''
 ^      行首匹配，和在[]里的 ^ 意思不同，它表示匹配以什么为开头的字符串
 $      行尾匹配，匹配以什么为结尾的字符串
'''

print(re.search("^he", "he is a good man"))
print(re.search("man$", "he is a good man"))

print('------------------')

# 匹配多个字符
r'''
(xyz)   匹配小括号里的xyz（xyz作为一个整体去匹配）
x?      匹配0个或1个x
x*      匹配0个或任意个x
'''

print(re.findall(r"(he)", "he is a good man, he he"))
print(re.findall(r"o?", "he is a good man, he he"))
print(re.findall(r"o*", "he is a good man, he he"))
print(re.findall(r"o+", "he is a good man, he he"))

str1 = "he is a good man she is not a good woman"
print(re.findall(r"he.+?man", str1))

# 电话号码
# 以 1 开头，第二位是3、5、7、8，后面9位都是数字，并且以数字结尾
pat = r"^1[3578]\d{9}$"
pat = r"^1(([3578]\d) | (47))\d{8}$"

