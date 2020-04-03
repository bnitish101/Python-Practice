
def bubble_sort(list):
    for iter_num in range(len(list) - 1, 0, -1):
        for indx in range(iter_num):
            if list[indx] > list[indx + 1]:
                temp = list[indx]
                list[indx] = list[indx + 1]
                list[indx + 1] = temp


list = [19, 2, 31, 45, 6, 11, 121, 27]
print(list)
bubble_sort(list)
print(list)
