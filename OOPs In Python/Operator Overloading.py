class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(2, 4)
s2 = Student(3, 4)

s3 = s1 + s2
print(s3.m1)
print(Student.__add__(s1, s2).m2)

if s1 > s2:
    print('S1 wins\n')
else:
    print('S2 wins\n')

print(type(s1))
print(s1)  # if print anything it'll automatically call __str__() magic method,
# class Student returns value of m1 and m2 in __str__() method which is overloading by inbuilt __str__() method

x = 2
y = '2'

print('\n', type(x))
print(type(y))
print(int.__str__(x))
print(str.__str__(y))
