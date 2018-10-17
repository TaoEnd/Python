# coding:utf-8

from multiprocessing import Pool
import os


def copyFile(sourcePath, targetPath):
	print("子进程%d开始" % os.getpid())
	fr = open(sourcePath, 'rb')
	fw = open(targetPath, 'wb')
	context = fr.read()
	fw.write(context)
	print("子进程%d结束" % os.getpid())

if __name__ == "__main__":
	source = r"E:\python\PythonSpace\Git\Python\ThreadProcess\test\source"
	target = r"E:\python\PythonSpace\Git\Python\ThreadProcess\test\target"
	fileList = os.listdir(source)
	print("父进程启动")
	p = Pool(3)
	for file in fileList:
		sourcePath = os.path.join(source, file)
		targetPath = os.path.join(target, file)
		p.apply_async(copyFile, args=(sourcePath, targetPath))
	p.close()
	p.join()
	print("父进程结束")
