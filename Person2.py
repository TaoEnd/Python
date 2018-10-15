# coding:utf-8

# 继承


class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def my_print(self):
		print(self.name, self.age)

	@property
	def get_name(self):
		return self.name


class man(Person):
	def my_print(self):
		# 在子类中显式的调用父类中的方法
		Person.my_print(self)
		# 首先调用父类中的方法，再调用子类中的同名方法
		print("my name", self.name)

m = man("张三", 18)
m.my_print()

