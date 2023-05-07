import glob
import pandas as pd

import warnings
# Warnings ignore command. Plenty of "future" warnings painting the console red
warnings.filterwarnings('ignore')

# Placing .pkl files into a list
shared_list_files = glob.glob('shared_customers/*.pkl')

# .pkl extraction as DataFrame to a list
shared_list_DataFrames = [pd.read_pickle(i) for i in shared_list_files]

# Proper col names vs bad ones, placing into a dict for renaming
b_col = [c for c in shared_list_DataFrames[5].columns]  # DF 5 is the bad file, specific case without scanning.
g_col = [c for c in shared_list_DataFrames[0].columns]
rename_col = {b_col[i]: g_col[i] for i in range(len(b_col))}

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


# plot
import matplotlib.pyplot as plt
city = pd.DataFrame(dfS['city'].value_counts())
ax = city.plot.bar(rot = 0)
# plot won't work help god


print()

# A fascinating way I found to detect the existence of at least 1 capital letters in any column name
# This can replace the manual detection I did for shared_customers_417
# for df in shared_list_DataFrames:
#     if max([max([s.isupper() for s in column_lst]) for column_lst in df.columns]):
#         print(f'Capital detected!')
#         print(df.columns)


