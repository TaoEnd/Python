#coding:utf-8

n = int(raw_input())
numList = map(int,raw_input().split())
i = n - 1
while(i>0):
	numList.sort()
	j = i - 1
	while(j>=0):
		if(numList[i]^numList[j] < numList[j]):
			numList[j] ^= numList[i]
		j -= 1
	i -= 1

count = 0
for x in numList:
	if(x != 0):
		count += 1

print count