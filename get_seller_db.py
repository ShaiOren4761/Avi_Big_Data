import pandas as pd
import random
import names


sellers = []
for i in range(20):
    sellers.append(names.get_full_name(random.choice(['male', 'female'])))
    # id is the index in the DataFrame
sellers = pd.DataFrame({'name': sellers})

sellers.to_pickle("my_supermarket\\my_sellers.pkl")

