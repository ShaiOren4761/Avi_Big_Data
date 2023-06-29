import random
import pandas as pd
import datetime
from faker import Faker

customers = pd.read_pickle("my_supermarket\\my_customer.pkl")
products = pd.read_pickle("my_supermarket\\product_db.pkl")
sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl")


def create_trade_date():
    fake = Faker()
    start_date = datetime.date(year=2023, month=1, day=1)
    date = fake.date_between(start_date=start_date, end_date='now')
    return date


def gen_trades_db():
    dic = {'tz': [], 'productS': [], 'date': [], 'payment_type': [],
           'total_pay': [], 'seller_id': []}
    for _ in range(random.randint(1500, 1700)):
        dic['tz'].append(customers.iloc[random.randrange(len(products))]['tz'])

        shopping_list = []
        for _ in range(random.randint(1, 20)):  # Shopping list generation
            rand_product = products.iloc[random.randrange(len(products))]
            amount = random.randint(1, 10)
            sub_total_price = rand_product['price']*amount
            product = {'id': rand_product['id'], 'amount': amount, 'price': sub_total_price}
            shopping_list.append(product)
        shopping_list = pd.DataFrame.from_dict(shopping_list)
        dic['productS'].append(shopping_list)
        dic['date'].append(create_trade_date())
        dic['payment_type'].append(random.randrange(4))
        dic['total_pay'].append(sum(shopping_list['price']))
        dic['seller_id'].append(random.randrange(len(sellers)))

    return pd.DataFrame.from_dict(dic)

# generation of a trades DB, OVERRIDES existing one in "my_supermarket"
# trades = trades_db()
# trades.to_pickle("my_supermarket\\my_trades.pkl")

