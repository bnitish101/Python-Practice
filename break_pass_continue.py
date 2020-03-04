# print numbers which are not divisible by 3 in a given range.
max = 50
start = 0
while start < max:
    if start % 3 != 0 or start % 5 != 0:
        print('Not divisible by 3 or 5 ', start)
    start = start + 1

# print number of candies given by user and quantity of candy is 6. if limit exceed print bye.
av = 6
# qty = int(input("How much candies do you want ?"))
qty = 10
i = 1
while i <= qty:
    if i > av:
        print('Out of stock')
        break
    print('Candy ', i)
    i = i + 1
print('Bye')


def fun(a):
    if a > 0:
        pass
        # print('Greater than Zer.')


fun(5)
