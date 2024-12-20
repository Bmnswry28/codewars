# https://www.codewars.com/kata/5419cf8939c5ef0d50000ef2
def calculate_probability(n):
    if n <=1:
        return 0.00
    
    probability = 1.0
    for i in range(365,365-n,-1):
        probability *= i / 365.0

    return round(1 - probability, 2 )