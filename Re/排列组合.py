# coding:utf-8

import itertools

# 排列
# 从列表[1,2,3,4]中选择3个元素，构成全排列
my_list = list(itertools.permutations([1, 2, 3]))
print(my_list)
print(len(my_list))

# 组合
my_list = list(itertools.combinations([1, 2, 3, 4], 2))
print(my_list)

# 排列组合
# 从[1, 2, 3, 4]（或者1234也可以）中选出3个数进行排列，可以有重复值
my_list = list(itertools.product([1, 2, 3, 4], repeat=3))
print(my_list)
print(len(my_list))
