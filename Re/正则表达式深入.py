# coding:utf-8

import re

r'''
re.finditer函数：与findall类似，扫描整个字符串，返回一个迭代器
'''

str1 = "he is man, he is people, he is person"
my_iter = re.finditer(r"(he)", str1)
while True:
	try:
		print(next(my_iter))
	except StopIteration as e:
		break

# 正则表达式编译成正则表达式对象
pat = r"^1(([3578]\d)|(47))\d{8}$"
re_telephone = re.compile(pat)
print(re_telephone.match("13912345678"))
