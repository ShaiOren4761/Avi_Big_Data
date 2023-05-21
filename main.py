from get_customer_db import gen_shared_customer
import pandas as pd

"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""
# creation of a customer DB, division into two seperate files, head 20% and tail 80%
# The two parts are made into files under shared_customers with the fitting % of split
# gen_shared_customer(dfS)

"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""

# Concatenation of all pkl's into a single pkl file
# from read_shared_customers import concat_customers
# concat_customers().to_pickle("my_supermarket\\my_customer.pkl")

# generation of sellers pkl
import dbs
dbs.seller_db()

# Reading the concatinated pkl file into a DataFrame
customers = pd.read_pickle("my_supermarket\\my_customer.pkl")
print()
