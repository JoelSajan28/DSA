from typing import List

def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    best = 0

    for price in prices:
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    
    return best
