import glob
import pandas as pd

import warnings
# Warnings ignore command. Plenty of "future" warnings painting the console red
warnings.filterwarnings('ignore')


def concat_customers():
    # Placing .pkl files into a list
    shared_list_files = glob.glob('shared_customers/*.pkl')

    # .pkl extraction as DataFrame to a list
    shared_list_DataFrames = [pd.read_pickle(i) for i in shared_list_files]

    # Proper col names vs bad ones, placing into a dict for renaming
    g_col = ['name', 'tz', 'age', 'gender', 'credit_company', 'city', 'entry_date']
    # for loop below scans for capital letters in all columns and changes the bad ones.
    for df in shared_list_DataFrames:
        if max([max([s.isupper() for s in column_lst]) for column_lst in df.columns]):
            # print(f'Capital detected!')
            # print(df.columns)
            temp = df.copy()
            b_col = [c for c in temp.columns]
            rename_col = {b_col[i]: g_col[i] for i in range(len(b_col))}
            df.rename(columns=rename_col, inplace=True)

    # renaming bad dataframes
    for df in shared_list_DataFrames:
        if 'Name' in list(df):
            df.rename(columns=rename_col, inplace=True)

    # Concatenating the DataFrames
    dfS = pd.concat(shared_list_DataFrames)  # , ignore_index=True)

    # gender cases fix
    dfS['gender'] = dfS['gender'].apply(lambda x: x.lower())

    # credit_company fix
    dfS['credit_company'] = dfS['credit_company'].apply(lambda x: x.lower())
    dfS['credit_company'].replace(['americanexpress', 'american express'], 'amex', inplace=True)
    # noinspection SpellCheckingInspection
    dfS['credit_company'].replace(['dieners'], 'diners', inplace=True)

    # entry_date fix
    dfS['entry_date'] = pd.to_datetime(dfS['entry_date'])
    dfS['entry_date'] = dfS['entry_date'].apply(lambda x: (x.month, x.year))

    # plot bar
    # from plots import create_graphs
    # clmn = "age"
    # plot = create_graphs(dfS, clmn)
    dfS.to_pickle('my_supermarket\\my_customer')


"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""
# creation of a customer DB, division into two separate files, head 20% and tail 80%
# The two parts are made into files under shared_customers with the fitting % of split
# gen_shared_customer(dfS)

"""
# DO NOT RUN PKL DB FILE CREATION - OVERRIDES EXISTING!!!
"""


