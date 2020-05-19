phone_1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 15}
phone_2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 10}
phone_3 = {'name': '', 'stock': 18, 'price': 10000, 'discount': 10}


def discounted(price, discount, max_discount=20, name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
    except ValueError:
        print("Please, check: we need int\\float in 'price', 'discount', 'max discount',"
              " and string at 'name'.")
    else:
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка.')
        if discount >= max_discount or 'iphone' in name.lower() or not name:
            return price
        else:
            return price - (price * discount / 100)

some_phone = discounted('asus', 10, name='asus')
print(some_phone)