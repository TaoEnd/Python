# coding:utf-8

from time import sleep


def run():
	while True:
		print("No")
		sleep(1.2)

if __name__ == "__main__":
	while True:
		print("Yes")
		sleep(1)
	# 因为一个程序是一个单任务，它只有一个进程，
	# 只有上面的while结束后才能执行run()
	run()

