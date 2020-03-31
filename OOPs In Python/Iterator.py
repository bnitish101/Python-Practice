# inbuilt iterator
nums = ['a', 'b', 'c', 'd']
it = iter(nums)
print(next(it))
print(it.__next__())

for i in it:
    print(i)


# lets create own iterator
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):  # this __iter__ method automatically called by for loop
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()
print(next(values))
print(next(values))
for v1 in values:  # for loop is used to call __iter__() indirectly, that is why we need to create __iter__() in class
    print(v1)
