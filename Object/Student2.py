# coding:utf-8


class Student:
	name = "NoName"
	age = 0

	def hello(self):
		print("大家好， 我是 %s，我今年 %s 岁了" %(self.name, self.age))

	def setName(self, name):
		self.name = name

	def setAge(self, age):
		self.age = age

# 实例化对象
lisi = Student()
lisi.setName("LiSi")
lisi.setAge(18)
lisi.hello()