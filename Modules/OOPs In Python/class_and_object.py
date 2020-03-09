class Computer:
    def config(self):
        print('i5, 8GB, 1TB')


comp1 = Computer()  # creating object
comp2 = Computer()  # Creating object

Computer.config(comp1)  # calling method of a class by passing object as parameter
Computer.config(comp2)  # calling method of a class by passing object as parameter

print('calling method in sort code, but meaning is same.')
comp1.config()
comp2.config()