class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3


s1 = Student(2, 4)
s2 = Student(3, 5)

s3 = s1 + s2
print(s3.m1)
print(Student.__add__(s1, s2).m2)

print(type(s1))

x = 2
y = '2'

int
print(type(x))
print(type(y))