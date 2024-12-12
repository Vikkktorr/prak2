from datetime import datetime

users = [
    {'username': 'user', 'password': '123', 'role': 'user', 'history': [], 'cart': []},
    {'username': 'admin', 'password': 'admin', 'role': 'admin'},
]

products = [
    {'id': 1, 'name': 'Кроссовки Nike Air Max', 'price': 12000, 'category': 'Обувь', 'brand': 'Nike', 'type': 'Кроссовки'},
    {'id': 2, 'name': 'Гантели 10 кг', 'price': 3000, 'category': 'Тренировочный инвентарь', 'brand': 'Adidas', 'type': 'Гантели'},
    {'id': 3, 'name': 'Футболка Adidas', 'price': 1500, 'category': 'Одежда', 'brand': 'Adidas', 'type': 'Футболка'},
    {'id': 4, 'name': 'Спортивные штаны', 'price': 4000, 'category': 'Одежда', 'brand': 'Nike', 'type': 'Штаны'},
    {'id': 5, 'name': 'Тренажер для пресса', 'price': 6000, 'category': 'Тренировочный инвентарь', 'brand': 'Generic', 'type': 'Тренажер'},
    {'id': 6, 'name': 'Рюкзак спортивный', 'price': 2500, 'category': 'Аксессуары', 'brand': 'Nike', 'type': 'Рюкзак'},
    {'id': 7, 'name': 'Спортивная бутылка', 'price': 800, 'category': 'Аксессуары', 'brand': 'Adidas', 'type': 'Бутылка'},
    {'id': 8, 'name': 'Шейкер для протеина', 'price': 500, 'category': 'Аксессуары', 'brand': 'Generic', 'type': 'Шейкер'},
]

def authenticate():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None

def change_password(user):
    while True:
        new_password = input("Введите новый пароль: ")
        confirm_password = input("Подтвердите новый пароль: ")
        if new_password == confirm_password:
            user['password'] = new_password
            print("Пароль успешно изменен.")
            break
        else:
            print("Пароли не совпадают. Попробуйте снова.")

def add_user():
    new_user = {}

    while True:
        username = input("Введите имя пользователя: ")
        if username:
            if any(user['username'] == username for user in users):
                print("Имя пользователя уже занято. Попробуйте другое.")
            else:
                new_user['username'] = username
                break
        else:
            print("Имя пользователя не может быть пустым.")

    while True:
        password = input("Введите пароль: ")
        confirm_password = input("Подтвердите пароль: ")
        if password == confirm_password:
            new_user['password'] = password
            break
        else:
            print("Пароли не совпадают. Попробуйте снова.")

    while True:
        role = input("Введите роль (user/admin): ").lower()
        if role in ('user', 'admin'):
            new_user['role'] = role
            break
        else:
            print("Неверная роль. Введите 'user' или 'admin'.")

    new_user['history'] = []
    new_user['cart'] = []
    new_user['created_at'] = datetime.now()
    users.append(new_user)
    print("Пользователь добавлен.")

def delete_user():
    display_users()
    while True:
        try:
            username_to_delete = input("Введите имя пользователя для удаления: ")
            user_to_delete = next((u for u in users if u['username'] == username_to_delete), None)
            if user_to_delete:
                users.remove(user_to_delete)
                print("Пользователь удален.")
                break
            else:
                print("Пользователь не найден.")
        except ValueError:
            print("Ошибка ввода.")


def edit_user():
    display_users()

    while True:
        username_to_edit = input("Введите имя пользователя для редактирования: ")

        user_to_edit = next((u for u in users if u['username'] == username_to_edit), None)

        if user_to_edit:
            print("\nТекущие данные пользователя:")
            print("-------------------------")
            print(f"Имя пользователя: {user_to_edit['username']}")
            print(f"Роль: {user_to_edit['role']}")


            new_username = input("Введите новое имя пользователя (или оставьте пустым для сохранения): ")
            user_to_edit['username'] = new_username or user_to_edit['username']

            while True:
                new_password = input("Введите новый пароль (или оставьте пустым для сохранения): ")
                if new_password:
                    confirm_password = input("Подтвердите новый пароль: ")
                    if new_password == confirm_password:
                        user_to_edit['password'] = new_password
                        break
                    else:
                        print("Пароли не совпадают. Попробуйте снова.")
                else:
                    break

            new_role = input("Введите новую роль (user/admin, или оставьте пустым для сохранения): ").lower()
            user_to_edit['role'] = new_role or user_to_edit['role']

            print("\nДанные пользователя успешно изменены.")
            break
        else:
            print("Пользователь не найден.")


def add_product(products):
    new_product = {}
    new_product['id'] = len(products) + 1
    new_product['name'] = input("Введите название товара: ")
    while True:
        try:
            new_product['price'] = float(input("Введите цену товара: "))
            if new_product['price'] <= 0:
                raise ValueError("Цена должна быть больше 0.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}")
    new_product['category'] = input("Введите категорию (Обувь, Одежда, Тренировочный инвентарь, Аксессуары): ")
    new_product['brand'] = input("Введите бренд: ")
    new_product['type'] = input("Введите тип товара: ")
    products.append(new_product)
    print("Товар добавлен.")


def delete_product(products):
    display_products(products)
    while True:
        try:
            product_id = int(input("Введите ID товара для удаления: "))
            product_to_delete = next((p for p in products if p['id'] == product_id), None)
            if product_to_delete:
                products.remove(product_to_delete)
                print("Товар удален.")
                break
            else:
                print("Товар не найден.")
        except ValueError:
            print("Ошибка ввода. Введите число.")


def search_products(products):
    search_term = input("Введите поисковый запрос (по названию): ").lower()
    results = [p for p in products if search_term in p['name'].lower()]
    display_products(results)


def filter_products(products):
    criteria = {}
    criteria['category'] = input("Введите категорию для фильтрации (или оставьте пустым): ") or None
    criteria['brand'] = input("Введите бренд для фильтрации (или оставьте пустым): ") or None
    criteria['type'] = input("Введите тип товара для фильтрации (или оставьте пустым): ") or None

    filtered_products = products
    for key, value in criteria.items():
        if value:
            filtered_products = list(filter(lambda p: value.lower() in p.get(key, '').lower(), filtered_products))
    display_products(filtered_products)


def display_products(products):
    if not products:
        print("Список товаров пуст.")
        return
    print("\nСписок товаров:")
    for product in products:
        print(f"{product['id']}. {product['name']} ({product['price']} руб.), Бренд: {product['brand']}, Тип: {product['type']}, Категория: {product['category']}")
        print("-" * 48)


def sort_products(products):

    while True:
        sort_by = input("Сортировать по (названию/цене): ").lower()
        if sort_by in ('названию', 'цене'):
            break
        print("Неверный параметр сортировки. Попробуйте ещё раз.")

    while True:
        reverse_str = input("Обратный порядок (да/нет): ").lower()
        if reverse_str in ('да', 'нет'):
            reverse = reverse_str == 'да'
            break
        print("Неверный параметр. Попробуйте ещё раз (да/нет).")

    if sort_by == 'названию':
        products.sort(key=lambda product: product['name'], reverse=reverse)
    elif sort_by == 'цене':
        products.sort(key=lambda product: product['price'], reverse=reverse)

    display_products(products)


def add_to_cart(user, products):
    while True:
        try:
            product_id = int(input("Введите ID товара для добавления в корзину: "))
            product = next((p for p in products if p['id'] == product_id), None)
            if product:
                user['cart'].append(product)
                print(f"Товар '{product['name']}' добавлен в корзину.")
            else:
                print("Товар не найден.")
            another_item = input("Добавить ещё товар в корзину? (да/нет): ").lower()
            if another_item == 'нет':
                break
        except ValueError:
            print("Неверный ID товара. Попробуйте снова.")


def view_cart(user):
    if not user['cart']:
        print("Корзина пуста.")
        return
    total_price = sum(product['price'] for product in user['cart'])
    print("\nВаша корзина:")
    for product in user['cart']:
        print(f"- {product['name']} ({product['price']} руб.)")
    print(f"\nОбщая стоимость: {total_price} руб.")


def edit_product(products):
    display_products(products)

    while True:
        try:
            product_id = int(input("Введите ID товара для редактирования: "))
            product_to_edit = next((p for p in products if p['id'] == product_id), None)

            if product_to_edit:
                print("\nТекущие данные товара:")
                print("-------------------------")
                print(f"ID: {product_to_edit['id']}")
                print(f"Название: {product_to_edit['name']}")
                print(f"Цена: {product_to_edit['price']}")
                print(f"Категория: {product_to_edit['category']}")
                print(f"Бренд: {product_to_edit['brand']}")
                print(f"Тип: {product_to_edit['type']}")

                new_name = input("Введите новое название (или оставьте пустым для сохранения): ")
                product_to_edit['name'] = new_name or product_to_edit['name']

                while True:
                    try:
                        new_price = input("Введите новую цену (или оставьте пустым для сохранения): ")
                        if new_price:
                            new_price = float(new_price)
                            if new_price <= 0:
                                raise ValueError("Цена должна быть больше 0.")
                            product_to_edit['price'] = new_price
                        break
                    except ValueError as e:
                        print(f"Ошибка: {e}")

                new_category = input("Введите новую категорию (или оставьте пустым для сохранения): ")
                product_to_edit['category'] = new_category or product_to_edit['category']

                new_brand = input("Введите новый бренд (или оставьте пустым для сохранения): ")
                product_to_edit['brand'] = new_brand or product_to_edit['brand']

                new_type = input("Введите новый тип (или оставьте пустым для сохранения): ")
                product_to_edit['type'] = new_type or product_to_edit['type']

                print("\nДанные товара успешно изменены.")
                break
            else:
                print("Товар не найден.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")


def display_users():
    if not users:
        print("Список пользователей пуст.")
        return
    print("\nСписок пользователей:")
    for user in users:
        print(f"- {user['username']} (роль: {user['role']})")


def analyze_statistics():
    if not users:
        print("Нет данных для анализа.")
        return

    product_popularity = {}
    user_count = {'user': 0, 'admin': 0}

    for user in users:
        user_count[user['role']] += 1
        for purchase in user.get('history', []):
            product = next((p for p in products if p['id'] == purchase['product_id']), None)
            if product:
                product_popularity[product['name']] = product_popularity.get(product['name'], 0) + 1

    print("\nСтатистика:")
    if product_popularity:
        print("Популярность товаров:")
        for product, count in product_popularity.items():
            print(f"- {product}: {count} покупок")
    else:
        print("Нет данных о покупках.")

    print("\nКоличество пользователей:")
    for role, count in user_count.items():
        print(f"- {role}: {count}")

def buy_from_cart(user, products):
    if not user['cart']:
        print("Ваша корзина пуста.")
        return

    total_price = sum(product['price'] for product in user['cart'])
    print(f"\nТовары в корзине (Общая стоимость: {total_price} руб.):")
    for i, product in enumerate(user['cart']):
        print(f"{i+1}. {product['name']} (ID: {product['id']}, Цена: {product['price']} руб.)")

    while True:
        choice = input("\nВведите номер товара для покупки (или 'все' для покупки всех товаров, или 0 для отмены): ").lower()
        if choice == '0':
            break
        elif choice == 'все':
            for product in user['cart'][:]:
                user['history'].append({'product_id': product['id'], 'name': product['name'], 'price': product['price'], 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            user['cart'].clear()
            print("Все товары успешно куплены!")
            break
        else:
            try:
                choice = int(choice)
                if 0 < choice <= len(user['cart']):
                    product = user['cart'].pop(choice - 1)
                    user['history'].append({'product_id': product['id'], 'name': product['name'], 'price': product['price'], 'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                    print(f"Товар '{product['name']}' успешно куплен!")
                else:
                    print("Неверный номер товара. Попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Введите номер товара или 'все'.")


def show_user_history(user):
    if not user['history']:
        print("История покупок пуста.")
        return

    print("\nИстория покупок:")
    for purchase in user['history']:
        print(f"- {purchase['date']}: {purchase['name']} (ID: {purchase['product_id']}, Цена: {purchase['price']} руб.)")

def reduce_prices_admin(products):
    while True:
        try:
            percentage = float(input("Введите процент снижения цен (0-100): "))
            if 0 <= percentage <= 100:
                for product in products:
                    reduction = product['price'] * (percentage / 100)
                    product['price'] = product['price'] - reduction
                print("Цены успешно уменьшены.")
                break
            else:
                print("Процент должен быть в диапазоне от 0 до 100.")
        except ValueError:
            print("Неверный ввод. Введите число.")

def main():
    while True:
        user = authenticate()
        if user:
            print(f"Вход выполнен. Ваша роль: {user['role']}")
            while True:
                print("\nМеню:")
                if user['role'] == 'user':
                    print("1. Фильтровать товары")
                    print("2. Сортировать товары")
                    print("3. Показать все товары")
                    print("4. Добавить в корзину")
                    print("5. Просмотреть корзину")
                    print("6. Изменить пароль")
                    print("7. Купить")
                    print("8. Показать историю покупок")
                    print("9. Найти товар")
                    print("10. Выход")
                else:
                    print("1. Добавить товар")
                    print("2. Удалить товар")
                    print("3. Изменить товар")
                    print("4. Найти товар")
                    print("5. Показать все товары")
                    print("6. Добавить пользователя")
                    print("7. Удалить пользователя")
                    print("8. Изменить данные пользователя")
                    print("9. Показать всех пользователей")
                    print("10. Анализ статистики")
                    print("11. Сделать скидку")
                    print("12. Выход")

                choice = input("Выберите действие: ")

                if user['role'] == 'user':
                    if choice == '1':
                        filter_products(products)
                    elif choice == '2':
                        sort_products(products)
                    elif choice == '3':
                        display_products(products)
                    elif choice == '4':
                        add_to_cart(user, products)
                    elif choice == '5':
                        view_cart(user)
                    elif choice == '6':
                        change_password(user)
                    elif choice == '7':
                        buy_from_cart(user, products)
                    elif choice == '8':
                        show_user_history(user)
                    elif choice == '9':
                        search_products(products)
                    elif choice == '10':
                        break
                    else:
                        print("Неверный выбор.")

                else:
                    if choice == '1':
                        add_product(products)
                    elif choice == '2':
                        delete_product(products)
                    elif choice == '3':
                        edit_product(products)
                    elif choice == '4':
                        search_products(products)
                    elif choice == '5':
                        display_products(products)
                    elif choice == '6':
                        add_user()
                    elif choice == '7':
                        delete_user()
                    elif choice == '8':
                        edit_user()
                    elif choice == '9':
                        display_users()
                    elif choice == '10':
                        analyze_statistics()
                    elif choice == '11':
                        reduce_prices_admin(products)
                    elif choice == '12':
                        break
                    else:
                        print("Неверный выбор.")

        else:
            print("Неверный логин или пароль.")


if __name__ == "__main__":
    main()
