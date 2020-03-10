# Type of Inheritance
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multiple Inheritance


class A:  # Super/Parent Class

    def feature1(self):
        print('Feature One is working.')

    def feature2(self):
        print('Feature Two is working.')


class B(A):  # Sub/Child Class of class A [Multilevel Inheritance]

    def feature3(self):
        print('Feature Three is working.')

    def feature4(self):
        print('Feature Four is working.')


class C:  # Super/Parent Class

    def feature5(self):
        print('Feature Five is working.')

    def feature6(self):
        print('Feature Six is working.')


class D(A, C):  # Sub/Child Class of Class A and Class C [Multiple Inheritance]

    def feature7(self):
        print('Feature Seven is working.')

    def feature8(self):
        print('Feature Eight is working.')


a1 = A()
a1.feature1()

print('Multilevel Inheritance', '\n')
b1 = B()
b1.feature1()
b1.feature3()

print('Multiple Inheritance', '\n')
d1 = D()
d1.feature2()
d1.feature8()