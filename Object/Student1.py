# coding:utf-8


class Student:
	# 属性
	name = "NoName"
	age = 0
	tel = "00000000"
	score = 0

	# 动作
	# self表示把对象自身传入函数
	def listen(self):
		print(self.name, self.score)

	def test(self, name, time, addr):
		pass


# 定义一个叫张三的学生
zhangsan = Student()
zhangsan.name = "zhangsan"
zhangsan.age = 18
zhangsan.tel = "12345678"
zhangsan.score = 85.5
zhangsan.listen()
zhangsan.test("python", "today", "classroom1201")

print(zhangsan.name, zhangsan.age)
