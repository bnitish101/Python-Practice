print('Fibonacci Series')


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print('Negative Num')
    elif n == 0:
        print(a)
    elif n == 1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a+b
            a = b
            b = c
            print(c)


fibonacci(10)