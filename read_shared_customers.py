import glob
import pandas as pd

# file listing
shared_list_files = glob.glob('shared_customers/*.pkl')

# pkl extraction as DataFrame to a list
shared_list_DataFrames = [pd.read_pickle(i) for i in shared_list_files]

# Proper col names vs bad ones, placing into a dict for renaming
b_col = [c for c in shared_list_DataFrames[5].columns]
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
dfS['credit_company'].replace(['dieners'], 'diners', inplace=True)


print()

# why does this not work - can't properly detect upper cases and act upon them
# for val in dfS['gender'].unique():
#     if [s.isupper() for s in val].any():
#         print(f'{val} has upper!')

"""""
months + years - convert the two foreign time type to a string containing the month / year
"""

