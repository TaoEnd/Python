# coding:utf-8

from multiprocessing import Process
from time import sleep


def run():
	print("子进程启动")
	sleep(3)
	print("子进程结束")

if __name__ == "__main__":
	print("父进程启动")
	p = Process(target=run)
	p.start()
	# 让父进程等待子进程结束后，再执行
	p.join()
	print("父进程结束")
