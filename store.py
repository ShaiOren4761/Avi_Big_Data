import pandas as pd
import analysis
import get_seller_db
import get_product_db
import get_customer_db
import read_shared_customers
import get_trades_db
import os
import matplotlib.pyplot as plt

from dbs import trades_db

plt.switch_backend('Qt5Agg')

run_mode = 'Analysis'  # 'AfterSharing'  #  'Init' #

if not os.path.isdir('stores'):
    os.mkdir('stores')

start_ind, numStoreS = 0, 10

main_path = 'stores'
shared_customer_path = f'{main_path}/shared_customer'

if run_mode == 'Init':

    directoryS = [main_path, shared_customer_path]

    for directory in directoryS:
        if not os.path.isdir(directory):
            os.mkdir(directory)
    get_product_db.gen(main_path)

    for store_ind in range(start_ind, numStoreS):
        store_name = f'{main_path}/store_{store_ind}'
        directoryS = [store_name, f'{store_name}/receipts']
        for directory in directoryS:
            if not os.path.isdir(directory):
                os.mkdir(directory)

        get_seller_db.gen_seller_db(store_name)
        shared_customer_name = f"{shared_customer_path}/shared_customer_{store_ind}.pkl"
        pkl80 = f"{store_name}/my_customer_80.pkl"
        get_customer_db.gen_shared_customer(pkl80, shared_customer_name)

elif run_mode == 'AfterSharing':
    read_shared_customers.concat_customers(main_path, shared_customer_path)
    for store_ind in range(start_ind, numStoreS):
        store_name = f'{main_path}/store_{store_ind}'
        pkl80 = f"{store_name}/my_customer_80.pkl"
        read_shared_customers.concat_80(pkl80, main_path, store_name)
        get_trades_db.gen_trades_db(store_name, main_path)
        print(f"store {store_ind} db's completed")

elif run_mode == 'Analysis':
    pass



print()

customer_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_customer.pkl')
    customer_dbs.append(df)

trades_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_trades.pkl')
    trades_dbs.append(df)

customer_no20_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_customer_80.pkl')
    customer_no20_dbs.append(df)

sellers_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_sellers.pkl')
    sellers_dbs.append(df)

products_db = pd.read_pickle('stores/product_db.pkl')

#for eachs store, bar graph for every seller how much money made


# for i in range(numStoreS):
#     plt.subplot(2, 5, i + 1)
#     analysis.store_best_seller(trades_dbs[i], sellers_dbs[i], i)

print()
