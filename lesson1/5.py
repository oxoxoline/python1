proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
staff = int(input('Введите колличество работников в фирме: '))

profit = proceeds - costs
profitability = (profit / proceeds) * 100  # Не пойму, почему не ставится %
revenue_per_employee = profit / staff

print(f'Выручка {proceeds},  Издержки {costs}, Количество работников {staff}')
print(f'Прибыль фирмы в расчете на одного сотрудника = {revenue_per_employee}')

if proceeds > costs:
    print('Выручка больше издержек. Рентабельность составила:', profitability, '%')  # Подставил % тут=)
elif proceeds < costs:
    print('Издержки больше выручки')
else:
    print('Выручка равна издержкам')
