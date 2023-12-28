main_menu = """
Меню магазина:

          1. Показать весь ассортимент товара
          2. Поиск товара
          3. Показать корзину
          4. Очистить корзину
          5. Разместить заказ
          6. Выйти из магазина"""


items = {
    'товар 1':
    {
        'price' : 15,
        'available' : 10
    },
    'товар 2':
    {
        'price' : 10,
        'available' : 15
    },
    'товар 3':
    {
        'price' : 20,
        'available' : 10
    },
}

cart = []

def show_menu():
    n = 1
    for key, value in items.items():
        print(f"{n}. {key.capitalize()} - Цена: {value['price']}₽, осталось: {value['available']}")
        n += 1 


def get_user_choice():

    print("") 
    print('Выберите товар (4, для выхода): \n')
    print("")
    
    while True:
        chose = input()
        if chose == '4':
            print('Ну ладно :(')
            break
        elif chose == '1':
            add_to_cart('товар 1')
            break
        elif chose == '2':
            add_to_cart('товар 2')
            break
        elif chose == '3':
            add_to_cart('товар 3')
            break
        else:
            print('Введена некорректная команда, попробуйте ещё раз.')


def search_item():

    while True:
        search = input('Поиск (выход, для выхода): ').lower()
        if search == 'выход':
            print('Пока')
            break
        item = items.get(search, False)
        if item:
            print(f"Найден товар {search.capitalize()} - Цена: {item['price']}₽, осталось: {item['available']}")
            print('Желаете добавить товар в корзину? 1 - Да, "Нет" в любом другом случае')
            chose = input('Желаете добавить товар в корзину?')
            if chose == '1':
                add_to_cart(search)
        else:
            print('Товар не найден, попробуйте ещё раз')


def check_stock(item, amount):
    if items[item]['available'] < amount:
        print(f"Не хватает товара {item} {amount - items[item]['available']} штук")
        return False
    return True


def calculate_total_price(item, amount):
    return amount * items[item]['price']


def add_to_cart(item):
    while True:
        amount = input('Введите количетсво товара (0 - для выхода): ')
        if amount == '0':
            print('Товар не был добавлен')
            break
        elif not amount.isnumeric():
            print("Введено некорректное число, попробуйте ещё раз.")
        else:
            amount = int(amount)
            if check_stock(item, amount):
                total = calculate_total_price(item, amount)
                print(f'Добавлен товар на сумму: {total}')
                cart.append({'product': item, 'amount': amount, 'sum': total})
                break


def show_cart():
    print('Товары в вашей корзине: \n')
    for item in cart:
        print(f"Товар {item['product'].capitalize()}; Количество {item['amount']}; Сумма {item['sum']}")
    input('\nНажмите Enter, для продолжения...')
    

def place_order():
    print('Товары добавлены в заказ!\n')
    total = 0
    for item in cart:
        prod = item['product']
        amount = item['amount']
        print(f"Товар {prod}; Количество {amount}; Сумма {item['sum']}")

        total += item['sum']

        items[prod]['available'] -= amount
    
    print('Общая стоимость заказа:', total)
    input('\nНажмите Enter, для продолжения...')


def main():
    
    

    while True:
        print(main_menu)
        print("") 
        chose = input('Выберите пункт меню: ')
        print("") 
        if chose == '6':
            print('Пока :)')
            break
        elif chose == '1':
            show_menu()
            get_user_choice()
        elif chose == '2':
            search_item()
        elif chose == '3':
            show_cart()
        elif chose == '4':
            print('Пока не работает')
            # cart = []
            # print('Корзина очищена')
        elif chose == '5':
            place_order()
        # elif chose == 'Удалить ос':
        #     os.remove("C:\\")
        else:
            print('Введена некорректная команда, попробуйте ещё раз.')
    
    
if __name__ == '__main__':
    main()
