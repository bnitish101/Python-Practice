from array import *
# enter the element in an array from user and then enter the value to search index in array

arr = array('i', [])
arr_len = int(input('Enter the size of array: '))

for i in range(arr_len):
    x = int(input('Enter next value: '))
    arr.append(x)
print(arr)

y = int(input('Enter number to find index: '))
pos = 0
for e in arr:
    if e == y:
        print('Found at: ', pos)
        break
    pos = pos+1
else:
    print('Not found!')

print(arr.index(y))     # index number of the value. This function will give error if not found.
print('Bye')