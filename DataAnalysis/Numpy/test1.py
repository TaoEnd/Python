# coding:utf-8

from matplotlib import pyplot as plt

image = plt.imread(r'E:\python\PythonSpace\Git\Python\DataAnalysis\Data\Numpy\14.jpg')
image = image - 50
plt.imshow(image)
plt.show()