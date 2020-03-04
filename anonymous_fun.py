def square(a):
    return a * a


res = square(5)
print(res)

# anonymous function
f1 = lambda a: a*a
res_f1 = f1(6)
print('Anonymous Function')
print(res_f1)


def add(a, b):
    return a + b


res1 = add(2, 3)
print(res1)

# Anonymous Function
f2 = lambda a, b: a+b
res_f2 = f2(2, 9)
print('Anonymous Function')
print(res_f2)