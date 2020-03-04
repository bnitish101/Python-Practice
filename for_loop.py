# print values of a list
print('print values of a list')
x = ['nio', 101, 1.5]
for i in x:
    print(i)

# print index and values both of a list
print('print index and values both of a list')
for k_v in range(len(x)):
    print(k_v, end="=> ")
    print(x[k_v])

# print all characters form given string
print('print all characters form given string')
name_str = 'Nitish'
for name_char in name_str:
    print(name_char)

# print range in revers order
print('print range in revers order')
for revers_number in range(20, 10, -1):
    print(revers_number)
# print number by gap of 2 in each iteration
print('print number by gap of 2 in each iteration')
for gap_of_2 in range(1, 10, 2):
    print(gap_of_2)

# print numbers which are not divisible by 5 in a range of 1 to 20 using for loop
print('print numbers which are not divisible by 5 in a range of 1 to 20 using for loop')
for j in range(1, 21):
    if j % 5 != 0:
        print('Not divisible by 5 is : ', j)
