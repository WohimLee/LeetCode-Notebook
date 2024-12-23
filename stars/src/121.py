

def leetcode121(prices: list):
    min_prices = 1e5
    max_profit = 0
    for i, price in enumerate(prices[:-1]):
        if price < min_prices:
            min_prices = price
            continue
        max_profit = max(price - min_prices, max_profit)
    return max_profit
        








if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]
    leetcode121(prices1)
    pass