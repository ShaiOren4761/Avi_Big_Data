import random
import pandas as pd

def trades_db(tz, products, seller_id):
    dic = {}
    for _ in range(1):
        dic['tz'] = random.choice(tz)
        dic['productS'] = {products}
        dic['date'].append(str(f'{random.choice([1, 12])}/{random.choice([2010, 2022])}'))
        dic['payment_type'].append(random.choice(['cash', 'credit']))
        dic['total_pay'] = sum(products.price)
        dic['spending_time'] = random.randint(5, 160)  # Total minutes customer spent in store
        dic['seller_id'].append(seller_id)

    return pd.DataFrame.from_dict(dic)