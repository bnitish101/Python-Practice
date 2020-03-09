class Computer:
    def __init__(self, comp, cpu, ram):
        self.comp = comp
        self.cpu = cpu
        self.ram = ram
        print('Hey ', comp, ' I am specially calling here!')

    def config(self, comp, cpu, ram):
        print()
        print('Config is: ', self.comp, ' ', self.cpu, ' ', self.ram)
        print('Config is: ', comp, ' ', cpu, ' ', ram)
        # print('Config is i5, 16GB')

    def test(self):
        print('Config is: ', self.comp, ' ', self.cpu, ' ', self.ram)


comp1 = Computer('comp1 Object', 'i8', '32GB')
comp2 = Computer('comp2 Object', 'AMD', '2GB')
test = Computer('test Object', 'testCPU', 'testRAM')
print('One')

Computer.config(comp1, 'LongComp1', 'i3', '4GB')
Computer.config(comp2, 'LongComp2', 'i5', '16GB')
print('Two')

comp1.config('SortCOmp1', 'i1', '128MB')
comp2.config('SortComp2', 'i2', '156MB')
print('Three')

test.test()
print('Four')