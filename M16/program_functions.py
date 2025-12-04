#Problem 4

def ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price
