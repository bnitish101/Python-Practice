# decorators can change the behaviour of existing function without changing code of existing function.
def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)
        else:
            return func(a, b)
    return inner


div1 = smart_div(div)
div1(4, 2)
