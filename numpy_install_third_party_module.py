from numpy import *

# there are Six ways to define array
# array
# linspace
# logspace
# arange
# zeros
# ones

print('array')
arr = array([33, -5, 12, 45, 34, -40], int)  # if not mention type it will auto declare depending upon values
print(len(arr))
print(arr)
print(arr.dtype)
print(type(arr))

print('arr_linspace')
arr_linspace = linspace(0, 12, 4)   # third parameter is parts, default part is 50
print(len(arr_linspace))
print(arr_linspace)
print(arr_linspace.dtype)
print(type(arr_linspace))

print('arange')
arr_arange = arange(1, 15, 2)   # third parameter will skip the range till the end
print(len(arr_arange))
print(arr_arange)
print(arr_arange.dtype)
print(type(arr_arange))

print('logspace')
arr_logspace = logspace(1, 40, 5)   # first and second para meter raise to 10 and then divide in parts by third parameter
print(len(arr_logspace))
print(arr_logspace)
print('%.2f' %arr_logspace[0])
print('%.3f' %arr_logspace[4])
print(arr_logspace.dtype)
print(type(arr_logspace))

print('ones')
arr_ones = ones(8)      # array of ones
print(arr_ones)

print('zeros')
arr_zeros = zeros(6)    # array of zeros
print(arr_zeros)