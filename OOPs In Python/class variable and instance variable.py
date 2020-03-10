class Car:
    wheel = 4  # Class/static Variable: inside the class but not in __init__ method

    def __init__(self):
        self.name = 'BMW'  # Instance Variable: inside the __init__ method
        self.mil = 20  # Instance Variable: inside the __init__ method


c1 = Car()
c2 = Car()

Car.wheel = 5  # this value will change for all objects/instance
print(c1.name, c1.mil, c1.wheel, Car.wheel)  # Class variable can call with object name or class name
print(c2.name, c2.mil, c2.wheel)
