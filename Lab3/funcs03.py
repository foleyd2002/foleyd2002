
def get_price(age):
    under_sixteen = 5
    over_sixty = 7
    remainder = 10
    if age < 16:
        return under_sixteen
    elif age >= 16 and age < 60:
        return remainder
    else:
        return over_sixty

print(get_price(55))