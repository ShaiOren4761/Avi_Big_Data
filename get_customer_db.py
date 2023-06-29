import names
import random
import pandas as pd


def customer_db():
    dic = {'name': [], 'tz': [], 'age': [], 'gender': [], 'credit_company': [], 'city': [], 'entry_date': []}
    for i in range(10000):
        dic['name'].append(names.get_full_name(random.choice(['male', 'female'])))
        dic['tz'].append(random.randint(100000000, 999999999))
        dic['age'].append(random.randint(10, 99))
        dic['gender'].append(random.choice(['male', 'female', 'other']))
        dic['credit_company'].append(random.choice(['Visa', 'Mastercard', 'AmericanExpress']))
        dic['city'].append(random.choice(['Afula', 'Haifa', 'Natanya', 'Krayot', 'Tel Aviv', 'Ashkelon', 'Rehovot',
                                          'Bat Yam', 'Beer Sheva', 'Bnei Brak', 'Ramat Gan', 'Jerusalem']))
        dic['entry_date'].append(str(f'{random.choice([1, 12])}/{random.choice([2010, 2022])}'))

    return pd.DataFrame.from_dict(dic)


def gen_shared_customer():
    df = customer_db()

    data = df.head(int(len(df) * 0.2))
    path = "shared_customers/shai_pickle20.pkl"
    data.to_pickle(path)

    data = df.tail(int(len(df) * 0.8))
    path = "shared_customers/shai_pickle80.pkl"
    data.to_pickle(path)





