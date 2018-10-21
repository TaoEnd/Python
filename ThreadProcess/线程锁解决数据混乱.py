# coding:utf-8

import threading

num = 0
lock = threading.Lock()


def run(n):
	global num
	for i in range(100000):
		# 上锁
		lock.acquire()
		try:
			num += n
			num -= n
		finally:
			# 开锁
			lock.release()
			
		# with lock:
		# 	num += n
		# 	num -= n

if __name__ == "__main__":
	t1 = threading.Thread(target=run, args=(2,))
	t2 = threading.Thread(target=run, args=(3,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("num =", num)