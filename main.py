from dbs import gen_product_db, gen_customer_db, gen_seller_db


df_pro = gen_product_db()
print(df_pro)

df_cus = gen_customer_db()
print(df_cus)

df_sell = gen_seller_db()
print(df_sell)




