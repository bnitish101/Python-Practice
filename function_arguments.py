def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print('x: ', x)


a = 10
print(id(a))
update(a)
print('a: ', a)


def update_lst(l):
    print(id(l))
    l[1] = 101
    print(id(l))
    print(l)


lst = [1, 2, 3, 4, 5]

print(id(lst))
print(lst)
update_lst(lst)

# Hence, In python there is no concept of pass by value or pass by reference
# when value gets change, new id is auto generated
