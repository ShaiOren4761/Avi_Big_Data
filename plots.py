import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('Qt5Agg')  # Enables creating new graphs in debug (interactive)


def create_graphs(dfS, clmn):
    vc = pd.DataFrame(dfS[clmn].value_counts())
    top = 20

    ax = vc.head(top).plot.bar(rot=30, title=f"Top {top} {clmn}")

    sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl") # Challenge, show top 20 salesmen.
    # top 20 bar graph with their names!
    plt.figure()
    plt.hist(dfS[clmn])
    plt.title(f"hist of {clmn}")
    plt.show()

    def print_receipt(trade_ind, trades, customers, sellers):
        with open(f'my_supermarket\\receipts\\receipt{trade_ind}.txt', 'w') as f:
            for k, v in trades.items():
                if k == 'tz':
                    bInd = customers[k] == v
                    v = customers[bInd]['name'].values[0]
                    k = 'customer name'
                elif k == 'seller_id':
                    v = sellers.iloc[v].values[0]
                    k = 'seller name'
                elif k == 'total_pay':
                    v = f'{v} NIS'
                f.write(f'{k}: {v}')
                f.write('\n')

