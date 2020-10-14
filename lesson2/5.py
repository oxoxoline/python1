some_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
user_element = int(input('Введите число: '))
el = 0

for i in some_list:
    if user_element <= i:
        el += 1
some_list.insert(el, user_element)
print(some_list)
