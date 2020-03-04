from array import *

vals = array('i', [1, 2, 3, -4, 8, 4, 2])

print(vals.buffer_info())   # size and address of an array
print(len(vals))            # size of array
print(vals.typecode)        # type of an array
print(vals)                 # value of array
print(type(vals))           # var type
print(id(vals))             # memory address of variable
vals.reverse()
print(vals)
print(vals[1])

for i in range(len(vals)):
    print(vals[i], end=' | ')

for e in vals:
    print(e)

print('copy array')
copy_arr = array(vals.typecode, (a*a for a in vals))    # square of each element
for e in copy_arr:
    print(e)


str_arr = array('u', ['N', 'i', 'o'])
for e in str_arr:
    print(e, end=' | ')