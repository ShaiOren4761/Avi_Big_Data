from dbs import gen_product_db
from get_product_db import get_dict_col
from pandas import DataFrame


test = gen_product_db()
dict_col = get_dict_col(test)

# print(test)
# print(stupid)
#
# print(f'{stupid["name"][9]} {stupid["id"][9]} {stupid["price"][9]}')


df = DataFrame.from_dict(dict_col)
print(df)

