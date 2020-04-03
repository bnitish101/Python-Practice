
def bubble_sort(list):
    for iter_num in range(len(list) - 1, 0, -1):  # start from last index since this index will be range of nested loop
        for indx in range(iter_num):  # this loop reduce the range as per the above index
            if list[indx] > list[indx + 1]:  # check from first index to the next index is greater than
                temp = list[indx]  # if condition true then swap the values using third variable
                list[indx] = list[indx + 1]
                list[indx + 1] = temp


list = [19, 2, 31, 45, 6, 11, 121, 27]
print(list)
print('----- cb+ -----')
bubble_sort(list)
print(list)
