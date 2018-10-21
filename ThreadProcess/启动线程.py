# coding:utf-8

import threading


def run():
	print("子线程（%s）启动" % threading.current_thread().name)
	print("子线程（%s）结束" % threading.current_thread().name)

if __name__ == "__main__":
	# 返回当前线程的实例
	print("主线程（%s）启动" % threading.current_thread().name)
	# name是给子线程的命名，存在默认值的
	t = threading.Thread(target=run, name="SubThread")
	t.start()
	t.join()
	print("主线程（%s）结束" % threading.current_thread().name)