def check_repeat(lst): # Takes a dict's keys and compares it to a set version of itself
    print(f' original list len: {len(lst)}, the set version has: {len(set(lst))}')


def gen_product_db():
    from get_product_db import get_product_db
    return get_product_db()


def gen_customer_db():
    from get_customer_db import customer_db
    return customer_db()


def gen_seller_db():
    from get_seller_db import seller_db
    return seller_db()


def gen_costumer_db():
    from get_customer_db import customer_db
    return customer_db()

def trades_db():
    from get_trades_db import trades_db
    return trades_db()

def seller_db():
    from get_seller_db import seller_db
    return seller_db()

