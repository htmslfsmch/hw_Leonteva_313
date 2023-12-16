from logic import *

if __name__ == '__main__':

    while True:

        action = int(input("Введите номер желаемого действия.\n"
                           "1. Покупка товара 2. Поиск Товара 3. Размещение заказа 4. Посмотреть корзину\n"))
        if action == 1:


            show_menu(warehouse)
            tuple_of_choice = get_user_choice()
            try:

                print(f"Цена за {tuple_of_choice[1]}: ", str(calculate_total_price(tuple_of_choice[0], tuple_of_choice[1])))
            except IOError:
                print("К сожалению, на складе нет достаточного количества товара")
                continue
            answer = input("Хотите добавить в корзину? да ИЛИ нет ")
            if answer == "да":
                add_to_card(tuple_of_choice[0], tuple_of_choice[1])

        elif action == 2:
            search_item()

        elif action == 3:
            for i in cart:
                #print(cart)
                if check_stock(i["name"]) == 0:
                    place_order(i["name"], i["amount"])
                    update_stock(i["name"], i["amount"])
            print("Заказ успешно размещен! Приходите к нам еще")
        elif action == 4:
            show_cart()
