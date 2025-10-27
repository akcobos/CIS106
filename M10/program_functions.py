#Problem 1 forecast function

def compute_forecast(month, sales):
    month = month.lower()
    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    elif month in ["oct", "nov", "dec"]:
        percent = 0.25
    else:
        percent = 0.0
    return sales * (1 + percent)

#Problem 2

import math

def wall_area_function(length, width, height):
    wall_area = 2 * length * height + 2 * width * height
    return math.ceil(wall_area)

def ceiling_area_function(length, width):
    ceiling_area = length * width
    return math.ceil(ceiling_area)

#Problem 3

def out_the_door_price (make, model, ev_code, msrp):
    
    if make.lower() == "honda" and model.lower() == "accord":
        discount_rate = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount_rate = 0.15
    elif ev_code.upper() == "Y":
        discount_rate = 0.30
    else:
        discount_rate = 0.05


    discounted_price = msrp * (1 - discount_rate)

    
    final_price = discounted_price * 1.07

    return round(final_price, 2)

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

#Problem 5

def assessed_value(county, market_value):
    county = county.lower()
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70


    value = market_value * percent
    return round(value, 2)



