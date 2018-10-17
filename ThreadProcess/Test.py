# coding:utf-8

from multiprocessing import Pool
import os

target = r"E:\python\PythonSpace\Git\Python\ThreadProcess\test\target"

def copyFile(li):
	print("子进程%d开始" % os.getpid())
	for path in li:
		name = path.split('\\')[-1]
		resultPath = target + '\\' + name
		fr = open(path, 'rb')
		fw = open(resultPath, 'wb')
		context = fr.read()
		fw.write(context)
	print("子进程%d结束" % os.getpid())

if __name__ == "__main__":
	source = r"E:\python\PythonSpace\Git\Python\ThreadProcess\test\source"
	fileList = os.listdir(source)
	nameList = []
	for file in fileList:
		nameList.append(os.path.join('%s\%s'%(source,file)))
	print("父进程启动")
	p = Pool(3)
	p.apply_async(copyFile, args=(nameList[:3],))
	p.apply_async(copyFile, args=(nameList[3:6],))
	p.apply_async(copyFile, args=(nameList[6:],))
	p.close()
	p.join()
	print("父进程结束")
