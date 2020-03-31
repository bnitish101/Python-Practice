# Method Overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, n1=None, n2=None, n3=None):
        res = 0
        if n1 != None and n2 != None and n3 != None:
            res = n1 + n2 + n3
        elif n1 != None and n2 != None:
            res = n1 + n2
        else:
            res = n1
        return res


s1 = Student(2, 3)
print(s1.sum(1, 2, 3))
print(s1.sum(10, 20))  # Method Overloading
print(s1.sum(50))  # Method Overloading
print(Student.sum(s1, 1, 2))  # Method Overloading


# Method Overriding
class A:
    def feature1(self):
        print('Feature1 A')


class B(A):
    def feature1(self):
        print('Feature1 B')


b1 = B()
# feature1 overriding of superclass
B.feature1(b1)  # className.methodName(objectNameOfClass)
b1.feature1()  # objectName.methodNameOfObjectOfClass
