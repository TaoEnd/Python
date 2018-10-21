#coding:utf-8

import sys

'''
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，
使得最后所有奶牛拥有的苹果数都相同，每一次，你只能从一只奶牛身上拿走
恰好两个苹果到另一个奶牛上，问最少需要移动多少次可以平分苹果，
如果方案不存在输出 -1。

每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100）
，接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。

输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。

输入：
4
7 15 9 5
输出：
3
'''

num = int(raw_input())
numList = map(int,raw_input().split())
sum = 0
for x in numList:
	sum += x
average = sum/num
if(average*num<sum):
	print(-1)
else:
	time = 0
	for x in numList:
		if(abs(x-average)%2==1):
			print(-1)
			sys.exit()
		else:
			time += abs(x-average)/2
	print time/2







