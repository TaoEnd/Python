#coding:utf-8

x,y = map(int,raw_input().split())
axis = [[0 for j in range(y)] for i in range(x)]

count = 0
i = 0
while i < x :
	j = 0
	while(j<y):

		if(i<2):
			if(j<2):
				axis[i][j] = 1
				count += 1
			elif(axis[i][j-2]!=1):
				axis[i][j] = 1
				count += 1
		else:
			if(j<2):
				if(axis[i-2][j]!=1):
					axis[i][j] = 1
					count += 1
			else:
				if(axis[i-2][j]!=1 and axis[i][j-2]!=1):
					axis[i][j] = 1
					count += 1
		j += 1
	i += 1

print count