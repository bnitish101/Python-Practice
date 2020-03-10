class Person:
    def __init__(self):
        self.name = 'Nio'
        self.age = 28

    def update(self):
        self.name = 'Nio101'
        self.age = 18

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


per1 = Person()
per1.update()
per2 = Person()

if per1.compare(per2):
    print('Same age.')
else:
    print('Different age.')

