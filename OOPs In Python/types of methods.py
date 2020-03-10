# Three types of method:
# 1. Instance Method: works with instance variables
# 2. Class Method: works with class/static variables
# 3. Static Method: doesnt work with both neither class/static variable nor instance variable


class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3):  # Instant method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod  # decorator for class method declare
    def school_info(cls):  # Class method
        return Student.school

    @staticmethod  # decorator for static method declare
    def getinfo():  # Static Method
        return 'This is Student class of abc Module.'


s1 = Student(21, 43, 12)
s2 = Student(34, 54, 45)

print(s1.m1, s1.m2, s1.m3)
print(s1.get_average())

print(s1.school_info())
print(s1.getinfo())