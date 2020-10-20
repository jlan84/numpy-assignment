import numpy as np
import matplotlib.pyplot as plt

def column_vector(n):
    return np.arange(n)

def random_array(r, c):
    return np.random.rand(r,c)

def color_replace(v):
    return np.where(v,'blue', 'red')

def compute_true_false_sums(x,b):
    dic = {}
    dic[True] = np.sum(x[b==True])
    dic[False] = np.sum(x[b==False])
    return dic

def select_from_two_arrays(x,y,b):
    return np.where(b,x,y)

def sum_of_squred_diff(x,y):
    return np.sum((x-y)**2)

if __name__ == "__main__":
    v = column_vector(3)
    print(v.shape)
    v2 = random_array(4,3)
    print(v2)
    x = np.array([0,0,1,0])
    print(color_replace(x))
    x = np.array([0,    1,    2,     3,    4,     5])
    b = np.array([True, True, False, True, False, False])
    print(compute_true_false_sums(x,b))
    x = np.array([1,    2,    3,     4,    5,     6])
    y = np.array([10,   20,   30,    40,   50,    60])
    b = np.array([True, True, False, True, False, True])
    print(select_from_two_arrays(x,y,b))
    x = np.array([0, 1, 0, 1, 0, 1])
    y = np.array([0, 1, 2, 3, 4, 5])
    print(sum_of_squred_diff(x,y))