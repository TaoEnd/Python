#coding:utf-8

#获取全排列
def getAllPermutation(result,left,n):
	if(n==len(left)):
		result.append(list(left))
	else:
		i = n
		while(i<len(left)):
			left[i],left[n] = left[n],left[i] #交换两个变量的值
			getAllPermutation(result,left,n+1)
			left[i],left[n] = left[n],left[i]
			i += 1

#判断是不是需要的排列
def isNeed(list1,left,n):

	numList = []
	for x in list1:
		numList.append(x)

	j = 0
	i = 0
	while(i<len(numList)):
		if(numList[i]==0):
			numList[i] = left[j]
			j += 1
		i += 1

	base = 0
	i = 0
	while(i<len(left)-1):
		j = i + 1
		while(j<len(left)):
			if(left[i]<left[j]):
				base += 1
			j += 1
		i += 1

	count = 0
	i = 0
	while(i<len(left)):
		j = 0
		first = True
		while(j<len(numList)):
			if(numList[j]==left[i]):
				first = False
			elif((first==True and numList[j]<left[i]) or (first==False and numList[j]>left[i])):
				count += 1
			j += 1
		i += 1

	if((count-base)==n):
		return True
	else:
		return False

n,k = map(int,raw_input().split())
numList = map(int,raw_input().split())
left = []
for i in range(1,n+1):
	left.append(i)
for x in numList:
	if(left.count(x)==1):
		left.remove(x)

base = 0
i = 0
while(i<len(numList)-1):
	j = i + 1
	while(j<len(numList)):
		if(numList[j]>numList[i] and numList[i] != 0):
			base += 1
		j += 1
	i += 1

result = []
getAllPermutation(result,left,0)

count = 0
i = 0
while(i<len(result)):
	if(isNeed(numList,result[i],k-base)==True):
		count += 1
	i += 1

print(count)



