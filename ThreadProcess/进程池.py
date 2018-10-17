# coding:utf-8

from multiprocessing import Pool
from time import sleep
import os
import random


def run(name):
	print("子进程%d启动--%s" % (name, os.getpid()))
	sleep(random.choice([1, 2, 3]))
	print("子进程%d结束--%s" % (name, os.getpid()))

if __name__ == "__main__":
	print("父进程启动")

	# 创建进程池
	# 表示可以同时执行4个进程，Pool默认进程数量是CPU核心数
	p = Pool(4)
	for i in range(6):
		# 创建进程并放入进程池，统一管理
		p.apply_async(run, args=(i,))
	# 关闭进程池，结束所有子进程
	# 在调用join前，必须先close，并且close后，不能再往进程池中添加新的进程
	p.close()
	# 进程池对象调用join，会等待所有子进程结束后才执行父进程
	p.join()
	print("父进程结束")
