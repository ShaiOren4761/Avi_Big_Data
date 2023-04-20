import glob
import pandas as pd

shared_list_files = glob.glob('shared_customers/*.pkl')

print(shared_list_files)

for i in shared_list_files:
    print(i)

shared_list_DataFrames = [pd.read_pickle(i) for i in shared_list_files]
print(shared_list_DataFrames)

concatenated = pd.concat(shared_list_DataFrames, ignore_index= True)

for file, df in zip(shared_list_files, shared_list_DataFrames):
    print(f'file: {file} is len {len(df)} and the columns are:{list(df)}')
print(concatenated)



