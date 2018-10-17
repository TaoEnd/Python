#coding:utf-8

X,Y = map(int,raw_input().split(" "))
count = [[0 for j in range(Y)] for i in range(X)]
dungeon = []
i = 0
while(i<X):
	line = raw_input()
	li = []
	for j in range(Y):
		li.append(line[j])
	dungeon.append(li)
	i += 1
#print 'over'
startX,startY = map(int,raw_input().split(" "))
#print startX ,startY
count[startX][startY] = 1
#print count
step = int(raw_input())
#print step
stepX = []
stepY = []
i = 0
while(i<step):
	line = raw_input().split(" ")
	stepX.append(int(line[0]))
	stepY.append(int(line[1]))
	i += 1
# print X,Y
# print count
# print dungeon
# print startX,startY
# print stepX,stepY

queueX = []
queueY = []
queueX.append(startX)
queueY.append(startY)

while(len(queueX)>0):
	startX = queueX.pop(0)
	startY = queueY.pop(0)
	j = 0
	while(j<step):
		if(startX+stepX[j]>=0 and startX+stepX[j]<X and startY+stepY[j]>=0 and startY+stepY[j]<Y):
			if(dungeon[startX+stepX[j]][startY+stepY[j]]=='.'):
				if(count[startX+stepX[j]][startY+stepY[j]]==0):
					count[startX+stepX[j]][startY+stepY[j]] = count[startX][startY] + 1
					queueX.append(startX+stepX[j])
					queueY.append(startY+stepY[j])
			else:
				count[startX+stepX[j]][startY+stepY[j]] = -1
		j += 1

value = 0
getOut = 0
for i in range(X):
	for j in range(Y):
		if(dungeon[i][j]=='.' and count[i][j]==0):
			getOut = 1
			break
		value = max(value,count[i][j])

if(getOut==1):
	print -1
else:
	print value-1