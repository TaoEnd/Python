# coding:utf-8

from multiprocessing import Process, Queue
import os
from time import sleep


def write(queue):
	print("启动写子进程%d" % os.getpid())
	for x in ["A", "B", "C", "D"]:
		queue.put(x)
		sleep(1)
	print("结束写子进程%d" % os.getpid())


def read(queue):
	print("启动读子进程%d" % os.getpid())
	while True:
		print("Value = " + queue.get(True))
	print("结束读子进程%d" % os.getpid())


if __name__ == "__main__":
	print("启动父进程")
	queue = Queue()
	pw = Process(target=write, args=(queue,))
	pr = Process(target=read, args=(queue,))
	pw.start()
	pr.start()
	pw.join()
	# 强制结束子进程
	pr.terminate()
	print("结束父进程")