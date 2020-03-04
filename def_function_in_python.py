def cb():
    print('Hello!')
    print('Hi cb+, How are you today?')


def add_sub(x, y):
    r1 = x + y
    r2 = x * y
    return r1, r2


cb()
result1, result2 = add_sub(5, 3)    # imp note : if function returns two values then variable must receive two values
print(result1, result2)
