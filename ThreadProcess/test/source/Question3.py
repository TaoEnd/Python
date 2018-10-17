#coding:utf-8
import sys

result = []
lines = sys.stdin
for line in lines:
	if(len(line.strip())==0):
		break
	result.extend(line.split(" "))
print(len(set(result)))
