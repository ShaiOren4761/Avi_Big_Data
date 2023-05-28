from get_customer_db import gen_shared_customer
import pandas as pd
import dbs

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
trades = pd.read_pickle("my_supermarket\\my_trades.pkl")
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

print()
