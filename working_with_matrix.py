from numpy import *

print('Working with matrix.')

arr = array([
    [1, 2, 3, 4, 5, 6, 9, 2, 3],
    [4, 5, 6, 7, 8, 2, 8, 9, 4]
])

print(arr.dtype)    # Datatype
print(arr.ndim)     # no. of Dimension
print(arr.shape)    # no. of rows and column
print(arr.size)

arr1 = arr.flatten()    # Convert One Dimension Array
print(arr1)

arr3 = arr1.reshape(3, 3, 2)
print(arr3)

# Matrices
print('Matrices')
new_arr = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]
])

m = matrix('1 2 3; 4 5 6; 7 8 9')
print(m)
print('Diagonal Values of Matrices')
print(diagonal(m))
print(m.min())
print(m.max())


m1 = matrix('1 2 4; 5 6 7; 8 9 10')
m2 = matrix('1 2 4; 5 6 7; 8 9 10')
print('First Matrices')
print(m1, end='')
print('Second Matrices')
print(m2)
print('Addition of matrices!')
m3 = m1 + m2
print(m3)

print('Multiplication of matrices')
m4 = m1 * m2
print(m4)