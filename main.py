from get_customer_db import gen_shared_customer
import pandas as pd
import trades_analysis


"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""
# creation of a customer DB, division into two separate files, head 20% and tail 80%
# The two parts are made into files under shared_customers with the fitting % of split
# gen_shared_customer(dfS)

"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""

# Concatenation of all pkl's into a single pkl file
# from read_shared_customers import concat_customers
# concat_customers().to_pickle("my_supermarket\\my_customer.pkl")

# generation of sellers pkl
# import get_seller_db as sellers # The mere import of the class makes the script run and perform all the actions within

# Reading the concatenated pkl file into a DataFrame
customers = pd.read_pickle("my_supermarket\\my_customer.pkl")
tradeS = pd.read_pickle("my_supermarket\\my_trades.pkl")
products = pd.read_pickle("my_supermarket\\product_db.pkl")
sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl")

import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')


# Product name column creation and appending to trades
for index, row in tradeS.iterrows():
    trade = row['productS']
    trade['name'] = trade['id'].apply(lambda x: products[x == products['id']]['name'].values[0])

# Customer name column creation and appending to trades
tradeS['customer_name'] = tradeS['tz'].apply(lambda x: customers[x == customers['tz']]['name'].values[0])
temp = tradeS.pop('customer_name')
tradeS.insert(0, 'customer_name', temp.values)


print()

trd = trades_analysis.TradesAnalysis(tradeS, customers, sellers)


trd.total_pay_return()


