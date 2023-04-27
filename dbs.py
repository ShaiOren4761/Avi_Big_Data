

def check_repeat(lst): # Takes a dict's keys and compares it to a set version of itself
    print(f' original list len: {len(lst)}, the set version has: {len(set(lst))}')


def gen_product_db():
    from get_product_db import get_product_db
    return get_product_db()


<<<<<<< HEAD
def gen_customer_db():
    from get_customer_db import customer_db
    return customer_db()


def gen_seller_db():
    from get_seller_db import seller_db
    return seller_db()
=======


def costumer_db():
    ret = {}
    for i in range(1):
        name = names.get_full_name(random.choice(['male', 'female']))
        tz = random.randint(100000000,999999999)
        age = random.randint(10, 99)
        gender = random.choice(['male', 'female'])
        credit_company = random.choice(['Visa', 'Mastercard', 'AmericanExpress'])
        city = random.choice(['Afula', 'Haifa', 'Natanya', 'Krayot', 'Tel Aviv', 'Ashkelon', 'Rehovot', 'Bat Yam',
                              'Beer Sheva', 'Bnei Brak', 'Ramat Gan', 'Jerusalem'])
        entry_date = str(random.choice(1, 12) + random.choice(2010, 2022))
>>>>>>> origin/master


# def trades_db():
#     tz?
#     productS = {id:amount}
#     date =
#     payment_type =
#     total_pay =
#     spending time =
#     seller_id =
#
# def seller_db():
#     name = names.get_full_name(random.choice(['male','female']))
#     id =
