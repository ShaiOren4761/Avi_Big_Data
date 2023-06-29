import pandas as pd
import trades_analysis
import get_seller_db
import get_product_db
import get_customer_db
import read_shared_customers
import get_trades_db
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

run_mode = 'AfterSharing'  # 'Init'  # 'AfterSharing' #
if run_mode == 'Init':
    print('Yalla good luck\n'
          'BEWARE: DB is being changed')
elif run_mode == 'ongoing':
    print('DB is already set')


if run_mode == 'Init':
    get_seller_db.gen_seller_db()
    get_product_db.gen()
    get_customer_db.gen_shared_customer()
elif run_mode == 'AfterSharing':
    read_shared_customers.concat_customers()
    get_trades_db.gen_trades_db()
elif run_mode == 'Analysis':
    pass

# Reading the concatenated pkl file into a DataFrame
customers = pd.read_pickle("my_supermarket\\my_customer.pkl")
tradeS = pd.read_pickle("my_supermarket\\my_trades.pkl")
products = pd.read_pickle("my_supermarket\\product_db.pkl")
sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl")

print()




