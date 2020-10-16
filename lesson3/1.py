def numbers_func(a, b):
    try:
        c = a / b
    except ZeroDivisionError as e:
        return e
    return a / b


print(numbers_func(int(input('Введите целое число: ')), int(input('Введите второе целое число: '))))
