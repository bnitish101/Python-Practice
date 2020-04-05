pos = 0


def linear_search(x, list):
    i = 0
    for val in list:
        if val == x:
            globals()['pos'] = i+1
            return True
        i = i+1
    return False


list = [19, 2, 31, 45, 6, 11, 121, 27]
x = 11
if linear_search(x, list):
    print('Found at ', pos)
else:
    print('Not Found')