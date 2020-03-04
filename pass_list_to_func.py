# Pass list to a function, count number of odd & even numbers in list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def odd_even_count(lst):
    odd = 0
    even = 0
    for i in lst:
        if i % 2 == 0:
            odd = odd + 1
        else:
            even = even + 1
    return odd, even


odd, even = odd_even_count(list)
print('Odd Count: ', odd)
print('Even Count: ', even)

print('String format to pass values')
print('Odd Count: {}, Event Count: {}'.format(odd, even))   # curly bracket will be replaced with values


print('Count name\'s character more than 5 latte in list')
list1 = ['Nitish', 'Anurag', 'Aila', 'Raj', 'Cb+']


def count_char(lst):
    mtf = 0
    ltf = 0
    for i in lst:
        if len(i) > 5:
            mtf = mtf+1
        else:
            ltf = ltf+1
    return mtf, ltf


more_than_five, less_than_five = count_char(list1)
print(more_than_five)
print(less_than_five)