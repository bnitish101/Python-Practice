# if function has yield instead of return known as Generator
def my_object():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'
    yield 'e'


ob1 = my_object()
print(next(ob1))
print(next(ob1))

print('-----------')


def sqrt_of_first_ten():
    n = 1
    while n <= 10:
        val = n*n
        yield val
        n += 1


print(next(sqrt_of_first_ten()))
print('-----------')
for i in sqrt_of_first_ten():
    print(i)