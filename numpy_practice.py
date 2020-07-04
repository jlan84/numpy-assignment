import numpy as np
import matplotlib.pyplot as plt

#1
def column_vector(n):
    return np.arange(0, n).reshape(n,1)

#2
def random_array(row, col):
    return np.random.rand(row,col)

#3
def color_replace(x):
    colors = np.array(['red', 'blue'])
    return colors[x]
#4
def compute_true_false_sums(x,b):
    dic = {}
    dic[True] = np.sum(x[b==True])
    dic[False] = np.sum(x[b==False])
    return dic

#5
def select_from_two_arrays(x, y, b):
    return np.where(b,x,y)
    
#6

def sum_of_squared_differences(x,y):
    return np.sum((x-y)**2)


## Advanced






if __name__=="__main__":
    print(column_vector(5))
    print(random_array(4,3))
    x = np.array([0, 0, 1, 0, 1]) 
    print(color_replace(x))
    x = np.array([0,    1,    2,     3,    4,     5])
    b = np.array([True, True, False, True, False, False])
    print(compute_true_false_sums(x, b))
    x = np.array([1,    2,    3,     4,    5,     6])
    y = np.array([10,   20,   30,    40,   50,    60])
    b = np.array([True, True, False, True, False, True])
    print(select_from_two_arrays(x, y, b))
    x = np.array([0, 1, 0, 1, 0, 1])
    y = np.array([0, 1, 2, 3, 4, 5])
    print(sum_of_squared_differences(x, y))