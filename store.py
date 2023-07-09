import pandas as pd
import get_seller_db
import get_product_db
import get_customer_db
import read_shared_customers
import get_trades_db
import os
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

run_mode = 'Analysis'  # 'AfterSharing'  #'Init'  #

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

products_db = pd.read_pickle('stores/product_db.pkl')
print()


for i in range(10):
    plt.subplot(2, 5, i+1)
    ax = customer_dbs[i]['age'].plot.hist(ec='black')
    ax = customer_no20_dbs[i]['age'].plot.hist(ec='black')
    plt.title(f'store {i}')
plt.suptitle('Stores age histogram')

# How many customers bought snacks
# What was their age at purchase?
# Anyone under 18, show the seller and the amount of sales he made

# Creation of a pure snack DataFrame
snack_list = ["Bamba", "Bisli", "Doritos", "Chitos", "Apropo", "Chips", "Pringles", "Kefli", "Popcorn"]
bInd = products_db['name'].apply(lambda x: any([snack in x for snack in snack_list]))
snacks_df = products_db[bInd]

trades_dbs[0].iterrows
for index, row in trades_dbs[0].iterrows():
    if row['productS'].apply(lambda x: ):
        print(f'{row["seller_id"]} sold snacks!')

