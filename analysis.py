import pandas as pd
import matplotlib.pyplot as plt
import trades_analysis
import matplotlib
matplotlib.use('Qt5Agg')


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

        # a = {}
        # for id in trade['id']:
        #     bInd = products['id']==id
        #     product = products[bInd]
        #     name = product['name'].values[0]
        #     # name = product['name'].values[0]
        #     a[id] = name

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


def product_name_col_addition_tradeS(tradeS):
    # Product name column creation and appending to trades
    for index, row in tradeS.iterrows():
        trade = row['productS']
        trade['name'] = trade['id'].apply(lambda x: products[x == products['id']]['name'].values[0])


def customer_name_col_addition_tradeS(tradeS, customers):
    # Customer name column creation and appending to trades
    tradeS['customer_name'] = tradeS['tz'].apply(lambda x: customers[x == customers['tz']]['name'].values[0])
    temp = tradeS.pop('customer_name')
    tradeS.insert(0, 'customer_name', temp.values)


