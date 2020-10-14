user_list = input('Напишите несколько слов через пробел: ').split()

for word in user_list:
    number_string = 0
    number_string += 1
    print(f'{number_string}) {word[:10]}')
