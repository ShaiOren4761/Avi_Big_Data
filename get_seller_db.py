import pandas as pd
import random
import names


def seller_db():
    dic = {'name': [], 'id': []}
    for i in range(1000):
        dic['name'].append(names.get_full_name(random.choice(['male', 'female'])))
        dic['id'].append(random.randint(100000000, 999999999))

    return pd.DataFrame.from_dict(dic)

