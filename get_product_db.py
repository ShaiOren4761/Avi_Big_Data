import pandas as pd
import random
import string


def get_dict_col(product_db):
    col_db = {'name': [], 'id': [], 'price': []}

    for key, items in product_db.items():
        col_db['name'].append(key)
        col_db['id'].append(items[0])
        col_db['price'].append(items[1])

    return col_db


def get_product_db():
    def gen_milk_db():
        dairy_names = ['milk', 'swiss_cheese', 'yellow_cheese', 'coco', 'carlo', 'milky', 'danone', 'yolo', 'butter',
                       'cream', 'sweet_cream', 'sour_cream', 'eggs', 'freedom_eggs', 'organic_eggs', 'Nepolian_cheese',
                       'almond_milk', 'goat_milk', 'melted_cheese', 'mozarella']

        dairy_dict = {}
        count = 1
        for i in range(1000):
            name = str(random.choice(dairy_names)) + str(count)
            id = random.randint(1000000000, 9999999999)
            price = random.randint(20, 400)
            dairy_dict[name] = [id, price]
            count += 1
        return dairy_dict

    def gen_snacks_db():
        def get_random_product_name(list):
            # choose from all lowercase letter
            listtoret = []
            for i in list:
                for j in range(111):
                    listtoret.append((i + str(j)))
            return listtoret

        def get_random_product_id():
            # choose from all lowercase letter
            numbers = string.digits
            result_id = ''.join(random.choice(numbers) for _ in range(10))
            return int(result_id)

        def get_random_prices():
            # choose from all lowercase letter
            price = random.uniform(1, 15)
            price = round(price, 2)
            return price

        listofcateg = ["Bamba", "Bisli", "Doritos", "Chitos", "Apropo", "Chips", "Pringles", "Kefli", "Popcorn"]
        snacks_db = {}
        for i in get_random_product_name(listofcateg):
            snacks_db[i] = [get_random_product_id(), get_random_prices()]
        snacks_db['Bisli666'] = [get_random_product_id(), get_random_prices()]
        return snacks_db

    def gen_bakery_db():
        bakery_db = {}
        bakery_prods = ["bread", "cake", "pizza", "prezel", "pita", "burekas", "bagget", "hala", "cookie", "pie", "dunats",
                        "baklawa", "lafa", "ziva", "jahnon", "lahuh"]

        count = 0
        for i in range(1000):
            name = str(random.choice(bakery_prods)) + str(count)
            id = random.randint(1000000000, 9999999999)
            price = random.randint(5, 20)
            bakery_db[name] = [id, price]
            count += 1

        return bakery_db


def get_dict_col(product_db):
    stupid_db = {'name': [], 'id': [], 'price': []}

    for key, items in product_db.items():
        stupid_db['name'].append(key)
        stupid_db['id'].append(items[0])
        stupid_db['price'].append(items[1])

    return stupid_db


