# find the enterd num is prime or not

num = int(input('Enter a number to check prime or not: '))

# mine
for i in range(num):
    if i > 1:
        if num % i == 0:
            print(num, ' is not a Prime number.')
            break
else:
    print(num, ' is a prime number')

print()
# tutorial
for i in range(2, num):
    if num % i == 0:
        print('Not Prime Number')
        break
else:
    print('Prime Number')