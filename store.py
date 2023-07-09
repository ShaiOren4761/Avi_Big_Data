import pandas as pd
import get_seller_db
import get_product_db
import get_customer_db
import read_shared_customers
import get_trades_db
import os
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')

run_mode = 'Analysis'  #  'AfterSharing'  # 'Init'  #

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


print() # סביבה עובדת = תמחק את הקוד פה למטה זה עשיתי לתרגול

customer_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_customer.pkl')
    customer_dbs.append(df)

trades_dbs = []
for i in range(numStoreS):
    df = pd.read_pickle(f'{main_path}/store_{i}/my_trades.pkl')
    trades_dbs.append(df)

print()

vc = customer_dbs[0]['age'].value_counts()
ax = vc.head(20).plot.bar()
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

vcS = []
for custDB in customer_dbs:
    vcS.append(custDB['age'].value_counts())

graph_dict = {}
for i, vc in enumerate(vcS):
    graph_dict[f'{i}'] = [vcS[i].iloc[69]]
df = pd.DataFrame.from_dict(graph_dict)
