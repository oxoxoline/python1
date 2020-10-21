from itertools import count, cycle


def my_func_count(start, stop):
    for x in count(start):
        if start >= stop:
            break
        else:
            print(x)


my_func_count(1, 3)

# С cycle() не разобрался

