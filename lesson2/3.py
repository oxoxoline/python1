user_number = int(input('Введите число от 1 до 12: '))

month_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
              7: 'summer', 8: 'summer', 9: 'fall', 10: 'fall', 11: 'fall', 12: 'winter'}

for key in month_dict:
    if user_number == key:
        print(month_dict.get(key))  # Сделал только для словаря

# user_number1 = int(input('Введите число от 1 до 12: '))
# month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 'winter', 'spring', 'summer', 'fall']
# for i in month_number:
# if user_number1 <= 2 or 12:
#     print('winter')
# elif user_number1 > 2 < 6:
#     print('spring')
# elif user_number1 > 6 < 9:
#     print('summer')
# else:
#     print('fall') # Код не рабочий =\
