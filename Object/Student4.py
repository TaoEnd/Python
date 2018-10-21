# coding:utf-8

# python中的变量是默认的共有变量


class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		# 私有变量的定义
		# 以两个下划线开头，但是不以下划线结果的变量就是私有变量
		# python中没有真正意义上的私有变量
		# python其实使用的是一种名字改变技术将私有变量的名字改变了而已
		# 所以用同样的名字时，你在外面访问不到它
		self.__dairy = self.name + "的日记"

	def hello(self):
		print("My name is %s, %s" %(self.name, self.__dairy))

lisi = Student("Lisi", 18)
lisi.hello()
# 通过这种方式可以访问私有变量
print(lisi._Student__dairy)
