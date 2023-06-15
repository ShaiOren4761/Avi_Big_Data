from get_customer_db import gen_shared_customer
import pandas as pd
import trades_analysis


"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""
# creation of a customer DB, division into two separate files, head 20% and tail 80%
# The two parts are made into files under shared_customers with the fitting % of split
# gen_shared_customer(dfS)

"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""

# Concatenation of all pkl's into a single pkl file
# from read_shared_customers import concat_customers
# concat_customers().to_pickle("my_supermarket\\my_customer.pkl")

# generation of sellers pkl
# import get_seller_db as sellers # The mere import of the class makes the script run and perform all the actions within

# Reading the concatenated pkl file into a DataFrame
customers = pd.read_pickle("my_supermarket\\my_customer.pkl")
tradeS = pd.read_pickle("my_supermarket\\my_trades.pkl")
products = pd.read_pickle("my_supermarket\\product_db.pkl")
sellers = pd.read_pickle("my_supermarket\\my_sellers.pkl")

import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')


# Product name column creation and appending to trades
for index, row in tradeS.iterrows():
    trade = row['productS']
    trade['name'] = trade['id'].apply(lambda x: products[x == products['id']]['name'].values[0])

# Customer name column creation and appending to trades
tradeS['customer_name'] = tradeS['tz'].apply(lambda x: customers[x == customers['tz']]['name'].values[0])
temp = tradeS.pop('customer_name')
tradeS.insert(0, 'customer_name', temp.values)


print()
def funnel(name, stage,text):
    import plotly.express as px
    data = dict(
        Amount=[total_pay, total_pay - sum(total_pay_per_r_customer), sum(total_pay_per_r_customer)],
        Type=["Total customers", "trades customers", "Returned"])
    fig = px.funnel(data, x='Amount', y='Type')
    fig.add_annotation(dict(font=dict(color='black', size=15),
                            x=0,
                            y=-0.12,
                            showarrow=False,
                            text=text,
                            textangle=0,
                            xanchor='left',
                            xref="paper",
                            yref="paper"))
    fig.show()
trd = trades_analysis.TradesAnalysis(tradeS, customers, sellers)

# data = dict(
#     Amount=[len(customers), tradeS['tz'].nunique(), len(trd.vc[trd.vc > 1])],
#     Type=["Total customers", "trades customers", "Returned"])
# data = dict(
#    Amount=[100, tradeS['tz'].nunique()/len(customers)*100, len(trd.vc[trd.vc > 1])/tradeS['tz'].nunique()*100],
#    Type=["Total customers", "trades customers", "Returned"])
# fig = px.funnel(data, x='Amount', y='Type')
# fig.show()

print()


# Long calculation of sum money I stole from trades_analysis
r_customers = trd.vc[trd.vc > 1]
total_pay_per_tz = tradeS.groupby('tz')['total_pay'].apply(lambda x: sum(x))  # All payments sum
total_pay_per_r_customer = total_pay_per_tz.loc[r_customers.index]  # All payment - funnel - returned customers
total_pay_r = sum(total_pay_per_r_customer)  # Sum of all returned customers' payments
total_pay = sum(total_pay_per_tz)  # Sum of all customers' payment

funnel([total_pay, total_pay-sum(total_pay_per_r_customer), sum(total_pay_per_r_customer)],
       ["Total customers", "trades customers", "Returned"],
f"{sum(total_pay_per_r_customer) / total_pay * 100}% of trades made is by the returning customers!")
# Long calculation of sum money I stole from trades_analysis

# adding names to the sellers in tradeS
temp = {"names": tradeS['seller_id'].apply(lambda x: sellers.iloc[x].values[0])}
tempFrame = pd.DataFrame.from_dict(temp)
tradeS.insert(6, 'seller_name', tempFrame)
