from functools import *
print('Filter Function')


def is_even(n):
    return n % 2 == 0


num = [1, 2, 3, 4, 62, 6, 13, 5]
evens = list(filter(is_even, num))
print(evens)
print('Using Lambda Function (Anonymous Function)')
evens_l = list(filter(lambda x: x % 2 == 0, num))
print(evens_l)

print('Map')


def double(n):
    return n * n


res = list(map(double, num))

print(res)

print('Using Lambda Function')

res_m = list(map(lambda a: a*a, num))
print(res_m)

print('Reduce')


def add_all(a,b):
    return a+b


res1 = reduce(add_all, num)
print(res1)
print('Using lambda')
res_r = reduce(lambda a, b: a+b, num)
print(res_r)