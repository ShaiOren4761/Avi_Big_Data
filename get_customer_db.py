import names
import random
import pandas as pd


def customer_db():  # The customers from the last 10 years
    dic = {'name': [], 'tz': [], 'age': [], 'gender': [], 'credit_company': [], 'city': [], 'entry_date': []}
    for i in range(100):
        dic['name'].append(names.get_full_name(random.choice(['male', 'female'])))
        dic['tz'].append(random.randint(100000000, 999999999))
        dic['age'].append(random.randint(10, 99))
        dic['gender'].append(random.choice(['male', 'female', 'other']))
        dic['credit_company'].append(random.choice(['Visa', 'Mastercard', 'AmericanExpress']))
        dic['city'].append(random.choice(['Afula', 'Haifa', 'Natanya', 'Krayot', 'Tel Aviv', 'Ashkelon', 'Rehovot',
                                          'Bat Yam', 'Beer Sheva', 'Bnei Brak', 'Ramat Gan', 'Jerusalem']))
        dic['entry_date'].append(str(f'{random.choice([1, 12])}/{random.choice([2010, 2022])}'))

    return pd.DataFrame.from_dict(dic)


def gen_shared_customer(pkl80, shared_customer_name):
    df = customer_db()

    data = df.head(int(len(df) * 0.2))  # shared customers
    data.to_pickle(shared_customer_name)

    data = df.tail(int(len(df) * 0.8))  # my customers
    data.to_pickle(pkl80)


def gen_storeS():
    NumOfStores = 10
    for store in range(NumOfStores):
        gen_shared_customer()

