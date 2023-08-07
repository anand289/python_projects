def find_profit(food_prices):
    max_diff = 0
    for i in range(0,len(food_prices)-1):
        for j in range (i+1, len(food_prices)):
            difference = food_prices[j] - food_prices[i]
            if difference > max_diff:
                max_diff = difference
                
    return max_diff


food_prices = [3,2,1]
print(find_profit(food_prices))