import pandas as pd
import trades_analysis
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')


def best_seller_check(df, sellers):
    total_pay_temp = 0
    manager_choice = input("for best seller, press 1 \nfor total sells, press 2 \nenter number: ")
    for seller in range(df["seller_id"].nunique()):
        seller_total_pay = 0
        for i in range(len(df.index)):
            if df["seller_id"][i] == seller:
                seller_total_pay += int(df["total_pay"][i])

        seller_name = sellers["name"][seller]
        if manager_choice == "2":
            print(f"{seller_name}, seller No. {seller}, sold a total of: {seller_total_pay}$")

        if total_pay_temp <= seller_total_pay:
            best_name = sellers["name"][seller]
            best_num = seller
            total_pay_temp = seller_total_pay
    if manager_choice == "1":
        print(f"the best seller is {best_name}, No. {best_num}")


def gen():

    trades = pd.read_pickle("my_supermarket/trades_db.pkl")
    ###############
    products = pd.read_pickle("my_supermarket/product_db.pkl")

    for index, row in trades.iterrows():
        # trade = trades.iloc[2]['products']#.copy()
        trade = row['products']#.copy()

        a = {}
        for id in trade['id']:
            bInd = products['id']==id
            product = products[bInd]
            name = product['name'].values[0]
            # name = product['name'].values[0]
            a[id] = name

        trade['name'] = trade['id'].apply(lambda x: products[x==products['id']]['name'].values[0])

        trade.drop('id', axis=1, inplace=True)

    customers = pd.read_pickle("my_supermarket/my_customer.pkl")
    sellers = pd.read_pickle("my_supermarket/seller_db.pkl")

    trd = trades_analysis.TradesAnalysis(trades, customers, sellers)

    # trd.print_receipts()
    trd.read_receipt(trade_ind=28)
    plt.figure()
    trd.trades_histogram()
    plt.figure()
    trd.trades_pie()
    trd.trades_funnel()
    trd.total_pay_return()

    plt.show()
    ##################

    sellers = pd.read_pickle("my_supermarket/seller_db.pkl")

    best_seller_check(trades, sellers)


# def product_name_col_addition_tradeS(tradeS):
#     # Product name column creation and appending to trades
#     for index, row in tradeS.iterrows():
#         trade = row['productS']
#         trade['name'] = trade['id'].apply(lambda x: products[x == products['id']]['name'].values[0])


def customer_name_col_addition_tradeS(tradeS, customers):
    # Customer name column creation and appending to trades
    tradeS['customer_name'] = tradeS['tz'].apply(lambda x: customers[x == customers['tz']]['name'].values[0])
    temp = tradeS.pop('customer_name')
    tradeS.insert(0, 'customer_name', temp.values)


def customer_age_col_addition_tradeS(tradeS, customers):
    # Customer name column creation and appending to trades
    tradeS['customer_age'] = tradeS['tz'].apply(lambda x: customers[x == customers['tz']]['age'].values[0])
    temp = tradeS.pop('customer_age')
    tradeS.insert(0, 'customer_age', temp.values)


def seller_name_col_addition(target_df, seller_df):
    target_df['seller_name'] = target_df['seller_id'].apply(lambda x: seller_df.iloc[x]['name'])
    temp = target_df.pop('seller_name')
    target_df.insert(0, 'seller_name', temp.values)


def store_best_seller(trades, sellers, store_ind):
    df_sellers_sum = trades.groupby('seller_id').sum()
    names = [sellers.iloc[ind]['name'] for ind in range(len(df_sellers_sum))]
    df_sellers_sum['seller_name'] = pd.DataFrame.from_dict(names)
    df_sellers_sum.sort_values(by= 'total_pay', ascending=True, inplace=True)
    plt.barh(df_sellers_sum['seller_name'], df_sellers_sum['total_pay'])
    plt.xticks(rotation=30)
    plt.savefig(f'stores/store_{store_ind}/total_pay.pdf')


def sellers_who_sold_snacks_to_minors(trades, customer_db, seller_db):
    # Creation of a pure snack DataFrame
    products_db = pd.read_pickle('stores/product_db.pkl')
    snack_list = ["Bamba", "Bisli", "Doritos", "Chitos", "Apropo", "Chips", "Pringles", "Kefli", "Popcorn"]
    bInd = products_db['name'].apply(lambda x: any([snack in x for snack in snack_list]))
    snacks_df = products_db[bInd]

    # snack_index = trades with snacks in productS
    snack_trades_index = []
    for index, row in enumerate(trades['productS']):
        if any(row['id'].apply(lambda x: any(x == snacks_df['id']))):
            snack_trades_index.append(index)

    # trades in which the age of the buyer was smaller than 18
    snacks_trades_df = trades.iloc[snack_trades_index]
    customer_age_col_addition_tradeS(snacks_trades_df, customer_db)
    underage_df = snacks_trades_df[snacks_trades_df['customer_age'] < 18]

    # Sellers who sold to snacks to minors
    seller_name_col_addition(underage_df, seller_db)
    return underage_df


def stores_age_histogram(customerS_list, customerS_80_list):
    for i in range(len(customerS_list)):
        plt.subplot(2, 5, i + 1)
        ax = customerS_list[i]['age'].plot.hist(ec='black')
        ax = customerS_80_list[i]['age'].plot.hist(ec='black')
        plt.title(f'store {i}')
    plt.suptitle('Stores age histogram')


def stores_basic_dashboard(trades_dbs):
    dc = {'store': [], 'unique customers': []}
    for index, trades in enumerate(trades_dbs):
        dc['unique customers'].append(trades['tz'].nunique())
        dc['store'].append(index)

    df = pd.DataFrame.from_dict(dc)

    plt.subplot(1, 2, 1)
    plt.bar(df['store'], df['unique customers'])
    plt.xticks(df['store'].keys())
    plt.title('unique customers per store')

    plt.subplot(1, 2, 2)
    plt.pie(df['unique customers'], labels=df['store'], shadow=True)
    plt.title('unique customers pie')
    plt.suptitle('STORE DASHBOARD')

    plt.savefig('stores/store_unique_customers_dashboard.pdf')


# def unique_customer_analysis():
#     for store in stores:
#         FileName = f'{main_path}/store_{store}/trades_db.pkl'
#         trades = pd.read_pickle(FileName)
#         utz = trades['tz'].unique()
#         len_utz = len(utz)
#         lenS.append(len_utz)


def analyzing_double_tz(dfS, shared_list_DataFrames, shared_list_files):
    for df, file in zip(shared_list_DataFrames, shared_list_files):
        if df['tz'].isin([496259402]).any():
            print(f'{file} has the duplicate tz!')
            vc = df["tz"].value_counts()
            bInd = df["tz"].value_counts() > 1
            double_tz = vc[bInd]
            print(f'{double_tz}')

    return double_tz


def ten_figures(df_list, store_ind):
    plt.figure()
    for i, df in enumerate(df_list):
        plt.subplot(2, 5, i+1)
        plt.hist(df['age'])
        plt.title(f'store {store_ind-1}')
        store_ind += 1
    plt.show()
# need an index and also a number that keeps track of position in overall DB.///


def homework(df_lst):
    lst = []
    store_ind = 1
    for df in range(len(df_lst)):
        lst.append(df_lst.pop(0))
        if len(lst) == 10:
            ten_figures(lst, store_ind)
            lst = []
            store_ind += 10
    if lst:
        ten_figures(lst, store_ind)

