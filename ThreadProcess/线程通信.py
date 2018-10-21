# coding:utf-8

import threading
import time


def fun():
	# 创建一个事件对象
	event = threading.Event()
	def run():
		for i in range(5):
			# 阻塞线程，等待事件被触发
			event.wait()
			# 重置，下一次还会继续阻塞
			event.clear()
			print("he is good")
	t = threading.Thread(target=run).start()
	return event

e = fun()
for i in range(5):
	# 触发事件
	e.set()
	time.sleep(2)