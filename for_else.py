# found the first num which is not divisible by Five
# here we can use else for 'for loop' called 'for else'
num = [11, 16, 18, 21, 25]

for i in num:
    if i % 5 == 0:
        print('Found!', i)
        break
else:
    print('Not Found!')
