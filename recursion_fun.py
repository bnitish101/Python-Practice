import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# recursion function means that function calling itself, default calling limit is 1000


def greet():
    print('Hello!')
    greet()


greet()