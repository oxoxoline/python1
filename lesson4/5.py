from functools import reduce


def my_func(x, y):
    return x * y


my_list = [x for x in range(100, 1001) if x % 2 == 0]

print(my_list)
print(reduce(my_func, my_list))
