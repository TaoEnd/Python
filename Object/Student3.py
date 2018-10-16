# coding:utf-8

# 构造函数和析构函数


class Student:
	# 构造函数
	# 1. 构造函数的写法固定
	# 2. self必须是第一个参数
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(name, age)

	def hello(self):
		print("大家好，我是%s，今年%s岁了。" %(self.name, self.age))

	# 析构函数
	def __del__(self):
		print("I am dead.")

# 对类进行实例化时，必须传入参数
lisi = Student("lisi", 18)
wangwu = Student("王五", 20)
wangwu.hello()
