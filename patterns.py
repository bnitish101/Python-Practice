# draw square pattern with hash # of 4*4
for j in range(4):
    for i in range(4):
        print('# ', end='')
    print()

print()
# print angle pattern start from top One Hash
for i in range(1, 5):
    for j in range(i):
        print('# ', end='')
    print()

print()
for i in range(4):
    for j in range(i+1):
        print('* ', end='')
    print()

print()
# print angle pattern start from top Four Hash

for i in range(4, 0, -1):
    for j in range(i):
        print('# ', end='')
    print()

print()
for i in range(4):
    for j in range(4-i):
        print('* ', end='')
    print()