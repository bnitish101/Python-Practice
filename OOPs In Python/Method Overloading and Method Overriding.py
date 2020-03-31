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
print(s1.sum(10, 20))
print(s1.sum(50))
print(Student.sum(s1, 1, 2))
