can = {'Склад': {}}
k = []
while True:
    a = input('выберите услугу: ')
    if a == 'add':
        product_name = input('Название: ')
        product_count = int(input('Кол-во: '))
        can['Склад'][product_name] = product_count
        print('Товар успешно добавлен!')
    elif a == 'delete':
        d = can.popitem()
        print(f'Товар {d} был успешно удалён!')
    elif a == 'inventory':
        print(can)
    elif a == 'buy':
        b = input('что брать ?: ')
        k.append(b)
        print('ваши товары успешно добалены в корзину!')
    elif a == 'delete_cart':
        z = k.pop()
        print(f'Покупка {z} была успешно удалена из корзины!')
    elif a == 'cart':
        print(k)
    else:
        print('ERROR')





