# inner class is define in side a class
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.Lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.Lap.show()

    class Laptop:  # inner class of Student class, inner class can call only inside the student class.
        def __init__(self):
            self.lap_brand = 'HP'
            self.lap_cpu = 'i5'
            self.lap_ram = '8GB'

        def show(self):
            print(self.lap_brand, self.lap_cpu, self.lap_ram)


s1 = Student('Nio', 93)

s1.show()
s1.Lap.show()  # can call like this too
