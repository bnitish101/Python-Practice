# print five time "Hello Word!" using while loop
i = 5;
while i >0:
    print('Hello World!', i)
    i = i-1

# print "Telusko" one and "Rocks" four times using nested loop
j=5
while j>0:
    print('Telusko ', end='')
    k=4
    while k>0:
        print('Rocks ', end='')
        k=k-1
    print()
    j=j-1