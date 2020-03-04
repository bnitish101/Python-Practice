from numpy import *
print('Copying Array.')

arr = array([2, 4, 6, 5, 8, 1, 10])
arr1 = arr          # Aliasing
arr2 = arr.view()   # Shallow Copy
arr3 = arr.copy()   # Deep Copy
arr[1] = 101

print(id(arr), end='')
print(arr)
print(id(arr1), end='')
print(arr1)
print(id(arr2), end='')
print(arr2)
print(id(arr3), end='')
print(arr3)