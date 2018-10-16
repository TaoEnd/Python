# coding:utf-8


class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		print(name, age, sex)

	# @property修饰的函数：定义时只要self参数
	# 调用时不要传递任何参数，并且不能写括号
	@property
	def get_age(self):
		pass


xiaohong = Person("小红", 18, "girl")
xiaoming = Person("小明", 18, "boy")
xiaoming.get_age

# dir()函数：返回当前范围内的变量、方法和定义的类型变量
print(dir())
print(dir(xiaohong))
print(xiaohong.__dict__)