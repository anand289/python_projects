def find_profit(food_prices):
    max_diff = 0
    for i in range(0,len(food_prices)-1):
        for j in range (i+1, len(food_prices)):
            difference = food_prices[j] - food_prices[i]
            if difference > max_diff:
                max_diff = difference
                
    return max_diff


food_prices = [10,12,14,12,13,11,8,7,6,13,23,45,11,10]
print(find_profit(food_prices))