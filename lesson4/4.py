some_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

sorted_list = [x for x in some_list if some_list.count(x) == 1]

print(sorted_list)

