# coding:utf-8

import threading

num = 0
local = threading.local()


def run(x, n):
	x += n
	x -= n


def func(n):
	# 给local对象设置一个x属性，并把全局变量赋值给该属性
	local.x = num
	for i in range(100000):
		run(local.x, n)
	print("%s - %d" % (threading.current_thread().name, local.x))

if __name__ == "__main__":
	t1 = threading.Thread(target=func, args=(2,))
	t2 = threading.Thread(target=func, args=(3,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("num =", num)