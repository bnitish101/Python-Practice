from numpy import *

print('Add 5 to all elements of an array')
arr = array([2, 4, 7, 3, 9])
arr_added = arr + 5
print(arr_added)

print('Add two arrays')
arr1 = array([34, 5, 6, 7, 2])
arr2 = array([1, 2, 3, 4, 5])
arr3 = arr1+arr2                #   Vectorized Operation
print(arr3)

print(arr)
print('square root of array')
print(sqrt(arr))
print('log of array')
print(log(arr))
print('sin of array')
print(sin(arr))
print('cos of array')
print(cos(arr))
print('max of array')
print(max(arr))
print('min value of array')
print(min(arr))
print('unique value of array')
print(unique(arr))
print('sum of array')
print(sum(arr))
print('concatenate arrays')
print(concatenate([arr1, arr2, arr3]))

print('copying array')
arr_copy = arr              # both array will refer same memory address [Aliasing]
print(arr)
print(arr_copy)

print(id(arr))
print(id(arr_copy))

arr_copy = arr.view()       # view will create new array to another memory even the values are same for both [Shallow Copy => if first array's value gets change it will that will change for both arraya]
print(arr)
print(arr_copy)

print(id(arr))
print(id(arr_copy))
print('Deep Copy')
arr_copy = arr.copy()              # both arrays are separate [Deep Copy => not link to each other at all]
print(arr)
print(arr_copy)

print(id(arr))
print(id(arr_copy))