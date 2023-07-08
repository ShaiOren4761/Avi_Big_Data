import pandas as pd
import trades_analysis
import get_seller_db
import get_product_db
import get_customer_db
import read_shared_customers
import get_trades_db
import os
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

run_mode = 'AfterSharing'  # 'Init'  # 'Analysis' #

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
    #read_shared_customers.concat_customers(main_path, shared_customer_path)
    for store_ind in range(start_ind, numStoreS):
        store_name = f'{main_path}/store_{store_ind}'
        pkl80 = f"{store_name}/my_customer_80.pkl"
        read_shared_customers.concat_80(pkl80, main_path, store_name)
        get_trades_db.gen_trades_db(store_name, main_path)

elif run_mode == 'Analysis':
    pass


print()




