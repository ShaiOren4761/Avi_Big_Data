import pandas as pd
from DataManagement import get_seller_db, get_product_db, get_customer_db, get_trades_db, read_shared_customers
import os
import matplotlib.pyplot as plt

plt.switch_backend('Qt5Agg')

run_mode = 'Analysis'  # 'AfterSharing'  # 'Init' #

if not os.path.isdir('stores'):
    os.mkdir('stores')

start_ind, numStoreS = 0, 23

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
    sellers_dbs = []
    customer_dbs = []
    trades_dbs = []
    customer_no20_dbs = []

    for i in range(numStoreS):
        customer_dbs.append(pd.read_pickle(f'{main_path}/store_{i}/my_customer.pkl'))
        trades_dbs.append(pd.read_pickle(f'{main_path}/store_{i}/my_trades.pkl'))
        customer_no20_dbs.append(pd.read_pickle(f'{main_path}/store_{i}/my_customer_80.pkl'))
        sellers_dbs.append(pd.read_pickle(f'{main_path}/store_{i}/my_sellers.pkl'))

    products_db = pd.read_pickle('stores/product_db.pkl')


print()


