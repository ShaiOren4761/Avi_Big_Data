import pandas as pd
import random
import names


def seller_db():
    sellers = []
    for i in range(20):
        sellers.append(names.get_full_name(random.choice(['male', 'female'])))
        # id is the index in the DataFrame
    return pd.DataFrame(sellers)

