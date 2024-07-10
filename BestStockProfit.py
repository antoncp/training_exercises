def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for price in prices[1:]:
        potential_profit = price - min_price
        if potential_profit > max_profit:
            max_profit = potential_profit
        if price < min_price:
            min_price = price

    return max_profit
