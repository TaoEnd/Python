# coding:utf-8

import threading
import queue
import time
import random


# 生产者，负责产生数据
def product(id, queue):
	while True:
		num = random.randint(0, 100)
		queue.put(num)
		print("生产者%d生产了%d数据" % (id, num))
		time.sleep(2)
	# 任务结束
	queue.task_done()


# 消费者，负责处理数据
def consumer(id, queue):
	while True:
		item = queue.get()
		if item is None:
			break
		else:
			print("消费者%d消费了%d" % (id, item))
		time.sleep(2)
	# 任务完成
	queue.task_done()

if __name__ == "__main__":
	# 消息队列
	q = queue.Queue()
	# 启动生产者
	for i in range(4):
		threading.Thread(target=product, args=(i, q)).start()
	# 启动消费者
	for i in range(3):
		threading.Thread(target=consumer, args=(i, q)).start()