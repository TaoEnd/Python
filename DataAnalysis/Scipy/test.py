# coding:utf-8
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from matplotlib import pyplot as plt
from scipy import fftpack as fft

path = r'E:\python\PythonSpace\Git\Python\DataAnalysis\Data\dog.jpg'
dog = plt.imread(path)
plt.imshow(dog, cmap="gray")
plt.show()