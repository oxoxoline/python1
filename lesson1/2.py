user_time = int(input('Введите время в секундах: '))

hours = user_time // 3600
minutes = (user_time % 3600) / 60
seconds = user_time % 60

print('%02d:%02d:%02d' % (hours, minutes, seconds))

