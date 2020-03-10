# Constructor in inheritance
# MRO (Method Resolution Order)


class A:
    def __init__(self):
        print('init in A')

    def feature1(self):
        print('Feature One-A is working.')

    def feature2(self):
        print('Feature Two-A is working.')


class B(A):
    def __init__(self):
        super().__init__()
        print('init in B')

    def feature3(self):
        print('Feature Three-B is working.')

    def feature4(self):
        print('Feature Four-B is working.')


class C:
    def __init__(self):
        print('init in C')

    def feature1(self):
        print('Feature One-C is working.')

    def feature2(self):
        print('Feature Two-C is working.')


class D(C, A):
    def __init__(self):
        super().__init__()  # this constructor call from C class since MOR(Method Resolution Order) LEFT to RIGHT. Hence C is in left and A is in right
        print('init in D')

    def feature7(self):
        print('Feature Seven-D is working.')

    def feature8(self):
        print('Feature Eight-D is working.')


print('\n', 'Constructor in multilevel inheritance')
b1 = B()
b1.feature3()

print('\n', 'Constructor in Multiple inheritance')
d1 = D()
d1.feature2()  # since feature2 exist in class A and class C. Since class C is in left that's why method will call from C towords MRO
