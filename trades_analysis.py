class TradesAnalysis:

    def __init__(self, trades, customers, sellers):
        self.trades = trades
        self.customers = customers
        self.sellers = sellers
        self.vc = trades['tz'].value_counts()

    def print_receipt(self):
        with open(f'my_supermarket\\receipts\\receipt{self.trade_ind}.txt', 'w') as f:
            for k, v in self.trades.items():
                if k == 'tz':
                    bInd = self.customers[k] == v
                    v = self.customers[bInd]['name'].values[0]
                    k = 'customer name'
                elif k == 'seller_id':
                    v = self.sellers.iloc[v].values[0]
                    k = 'seller name'
                elif k == 'total_pay':
                    v = f'{v} NIS'
                f.write(f'{k}: {v}')
                f.write('\n')

    def read_receipt(self, trade_ind):
        with open(f'my_supermarket\\receipts\\receipt{trade_ind}.txt') as f:
            print(f.read())
        # receipt generation
        # for trade_index in range(len(tradeS)):
        #     trade = tradeS.iloc[trade_index]
        #     print_receipt(trade_index, trade, customers, sellers)

    def trades_histogram(self):
        self.trades['customer_name'].value_counts().plot.hist()

    def trades_funnel(self):
        vc = self.trades['customer_name'].value_counts()
        vcReturn = vc[vc.values > 1]
        # vcNotReturn = vc[vc.values == 1]

        # info funnel
        print(f"trades amount = {self.trades.__len__()}")
        print(f"difference from potential costumers {round(len(vc)*100/len(self.customers),2)}%")
        print(f"unique costumers = {self.trades['customer_name'].nunique()}")
        print(f"unique costumers = {round(vcReturn.__len__() * 100 / self.trades['customer_name'].nunique(), 2)}"
              f"% returned")

    def trades_pie(self):
        self.vc.value_counts().plot.pie()

    def total_pay_return(self):  # percentage of payment made by returning customers and one-time customers
        r_customers = self.vc[self.vc > 1]

        total_pay_per_tz = self.trades.groupby('tz')['total_pay'].apply(lambda x: sum(x))  # All payments sum
        total_pay_per_r_customer = total_pay_per_tz.loc[r_customers.index]  # All payment - funnel - returned customers
        total_pay_r = sum(total_pay_per_r_customer)  # Sum of all returned customers' payments
        total_pay = sum(total_pay_per_tz)  # Sum of all customers' payment
        print(f'total_pay_r: {total_pay_r} [{round(total_pay_r / total_pay * 100, 2)}%]')
        # I've got to fix this mess, works on Avi's side, and it makes sense. But I copied without understanding.
