# coding:utf-8

import itertools

my_iter = ("".join(x) for x in itertools.product("1234", repeat=2))
while True:
	try:
		print(next(my_iter))
	except StopIteration as e:
		break
