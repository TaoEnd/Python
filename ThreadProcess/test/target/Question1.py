#coding:utf-8

n = int(raw_input())
#将输入按照空格进行划分，并且每个值转化成整数
arr = map(int,raw_input().split())
K,D = map(int,raw_input().split())

print K,D

#创建一个n行k列的二维数组，并且没每一个元素赋上0的初值
fm = [[0 for j in range(K)] for i in range(n)]
fn = [[0 for j in range(K)] for i in range(n)]
value = 0
#当选择的学生是第i个时
for i in range(n):
	#初始化矩阵的第一列
	fm[i][0] = fn[i][0] = arr[i]
	#动态规划，选择第2个学生时、选择第3个学生时...（0代表第一个学生）
	for k in range(1,K):  #表示k的取值范围为[1，K)
		#当我选定的第k个学生是i时，那么第k-1个学生的选择的范围只能在[0,i-1]或者
		#[i-D,i-1]之内，fm只存大的值，fn只存小的值
		for j in range(max(0,i-D),i):
			fm[i][k] = max(fm[i][k],max(fm[j][k-1]*arr[i],fn[j][k-1]*arr[i]))
			fn[i][k] = min(fn[i][k],min(fm[j][k-1]*arr[i],fn[j][k-1]*arr[i]))
	value = max(value,fm[i][K-1])
print value
