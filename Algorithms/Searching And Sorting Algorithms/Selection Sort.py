def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp


list = [19, 2, 31, 45, 6, 11, 121, 27]

print(list)
selection_sort(list)
print(list)
