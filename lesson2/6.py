list_product = []
number_product = 0

while number_product <= 1:
    name_product = input('Введите название товара: ')
    cost_product = int(input('Введите цену товара: '))
    amount_product = int(input('Введите количество товара: '))
    unit_product = input('Введите еденицы измерения: ')
    number_product += 1
    list_product.append(name_product), list_product.append(cost_product),
    list_product.append(amount_product), list_product.append(unit_product)
    # print(f'{number_product}) {name_product}, {cost_product}, {amount_product}, {unit_product}')
print(list_product)

# Не понял как сделать список со вложенными кортежами и словарями внутри
