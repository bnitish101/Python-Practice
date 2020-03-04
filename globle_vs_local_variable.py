a = 10


def update():
    a = 8       # using local variable
    print('In fun: ', a)


update()

print('Out fun: ', a)

a1 = 10


def update1():
    global a        # using global variable1
    a1 = 8
    print('In fun1: ', a1)


update1()
print('Out fun1: ', a1)


a2 = 10
print(id(a2))
b2 = 0
c2 = 0


def update2():      # Global and Local variable in the same fun
    a2 = 15         # Local var
    x2 = globals()['a2']    # Global var
    print(id(x2))
    print('In fun2: ', x2)
    print('In fun: ', a2)
    globals()['a2'] = 101   # update global var


update2()
print('Out fun2: ', a2)