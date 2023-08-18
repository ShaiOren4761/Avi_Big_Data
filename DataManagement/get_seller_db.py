import pandas as pd
import random
import names


def gen_seller_db(store_name):
    sellers = []
    for i in range(20):
        sellers.append(names.get_full_name(random.choice(['male', 'female'])))  # id is the index in the DataFrame
    sellers = pd.DataFrame({'name': sellers})
    sellers.to_pickle(f"./{store_name}/my_sellers.pkl")

