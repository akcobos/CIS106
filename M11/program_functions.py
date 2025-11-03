#Problem 1 Function

def calculate_discount(quantity, price, discount_rate):
    total = quantity * price
    discount_amount = total * discount_rate
    discounted_price = total - discount_amount
    return round(discount_amount, 2), round(discounted_price, 2)

#Problem 2 Function

def compute_scores(exam1, exam2, exam3):
    total = exam1 + exam2 + exam3
    average = total / 3
    return total, round(average, 2)

#Problem 3 Function

def compute_sales_metrics(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    next_year_target = sales * 0.05
    return commission, next_year_target

#Problem 4 Function

def compute_bowling_scores(score1, score2, score3, handicap):
    average = (score1 + score2 + score3) / 3
    adjusted_average = average + handicap
    return average, adjusted_average



#Problem 5 Function

#Global variables
total = 0
tax = 0

def compute_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07
