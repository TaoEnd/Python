# coding:utf-8
from multiprocessing import Process
from time import sleep
import os


def run(str1):
	while True:
		# os.getpid()获取当前进程ID
		# os.getppid()获取当前进程的父进程ID
		print("No %s %s %s" % (str1, os.getpid(), os.getppid()))
		sleep(1.2)

if __name__ == "__main__":
	print("主进程启动")

	# 在当前的进程中创建一个子进程
	# target说明进程要执行的任务，即它执行哪段代码
	# args是传递的参数，它是一个元组，只有一个元素的时候，最后要使用逗号
	p = Process(target=run, args=("nice", ))
	# 启动进程
	p.start()

	while True:
		print("Yes %s" % os.getpid())
		sleep(1)
