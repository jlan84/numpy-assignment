import numpy as np

def row_or_column_means(m, label='row'):
    if label == 'row':
        return np.mean(m,axis=1)
    if label == 'column':
        return np.mean(m, axis=0)

def ones_above_and_below_diagonal(n):
    m = np.zeros((n,n), dtype=int)
    np.fill_diagonal(m[1:,:], 1)
    np.fill_diagonal(m[:,1:], 1)
    return m

def checkerboard(n):
    m = np.zeros((n,n), dtype=int)
    m[::2,::2] = 1
    m[1::2,1::2] = 1
    return m

def ones_border(n):
    m = np.zeros((n,n), dtype=int)
    m = np.pad(m,pad_width=1, mode='constant',constant_values=1)
    return m

def negative_columns(m):
    columns = np.any(m<0, axis=0)
    return m[:,columns]

def get_closest_idx(m,n):
    m1 = np.abs(m - n)
    return np.argmin(m1), m1

def subtract_row_means(m):
    means = np.mean(m, axis= 1).reshape(m.shape[0],1)
    return m - means

if __name__ == "__main__":
    X = np.array([[0, 1], [2, 1]])
    print(row_or_column_means(X, label="row"))
    print(row_or_column_means(X, label="column"))
    print(ones_above_and_below_diagonal(5))
    print(checkerboard(5))
    print(ones_border(5))
    m = np.random.randint(-2,10,20).reshape(-1,4)
    print(m)
    print(negative_columns(m))
    m = np.random.randint(100, size=10)
    print(m)
    print(get_closest_idx(m,11))
    m = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 2, 3, 4]])
    print(subtract_row_means(m))

    