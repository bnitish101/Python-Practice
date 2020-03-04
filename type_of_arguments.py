# Formal Arguments

# Actual Arguments
#     Position
#     Default
#     Keyword
#     Length


def person(name, age):
    print(name)
    print(age - 5)


def person_dflt(name, age=18):
    print(name)
    print(age - 2)


person('Nio', 28)   # Position argument
print('Keyword Argument')
person(age=28, name='Nio')  # Keyword argument
print('Default Age')
person_dflt('Nio')


print('Lengnt Argument Functions')


def add_nums(a, *b):
    c = a
    for i in b:
        c = c+i
    print(c)


def add_nums1(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


print('Length argument')
add_nums(1, 2, 3, 4, 5)
add_nums1(1, 2, 3, 4, 5)


print('Keyworded Variable Length Arguments')


def person_det(name, **data):
    print(name)
    for i,j in data.items():
        print(i, j)


person_det('Nio', age=28, address='Mumbai')
