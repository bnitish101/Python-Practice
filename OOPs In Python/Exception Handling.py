a = 6
b = 2
try:
    print('Resource Opened.')
    print(a/b)
    k = int(input('Enter a number: '))
    print(k)
except ZeroDivisionError as e:
    print('You can not divide a num by zero! ', e)
except ValueError as e:
    print('Invalid Value.')
except Exception as e:
    print('Something went wrong...')
finally:
    print('Resource closed.')