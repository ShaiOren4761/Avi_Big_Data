
def analyzing_DoubleTz(dfS, shared_list_DataFrames, shared_list_files):
    for df, file in zip(shared_list_DataFrames, shared_list_files):
        if df['tz'].isin([496259402]).any():
            print(f'{file} has the duplicate tz!')
            vc = df["tz"].value_counts()
            bInd = df["tz"].value_counts() > 1
            double_tz = vc[bInd]
            print(f'{double_tz}')

    return double_tz
