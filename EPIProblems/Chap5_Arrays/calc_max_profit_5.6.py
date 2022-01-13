"""
EPI Problem 5.6: Find the max profit in buying and selling a stock one time.
Stock needs to be purchased prior to selling.

Eg. 310, 315, 275, 295, 260, 270, 290, 230, 255, 250
    => Max profit of 30 is obtained when purchasing at 260 and selling at 290
"""

"""
Solution: The max profit is not necessarily max price - min price since min price could be after max price.
Tip: Start with max_profit as 0 and min_price set to the first price. As you walk through the list of prices,
     adjust max_profit using min_price as the purchase price; adjust min_price as need be.
"""

def calculate_max_profit(prices):
    max_profit, min_pp, pp, sp = 0, prices[0], 0, 0
    for idx in range(1, len(prices)):
        cp = prices[idx]
        if cp > min_pp:
            profit = cp - min_pp
            if profit > max_profit:
                pp, sp, max_profit = min_pp, cp, profit
        elif cp < min_pp:
            min_pp = cp
    return pp, sp, max_profit

"""
Test code
"""
if __name__ == "__main__":
    stock_prices = [
        [100, 150, 125, 155, 75, 100, 110, 120, 150, 130, 200, 175],
        [310, 315, 275, 295, 260, 270, 290, 230, 255, 250],
        [100, 200, 300, 400, 500, 600, 700, 800],
        [1000, 900, 800, 700, 600, 500, 400, 300],
    ]
    for sp in stock_prices:
        print("Stock Prices: {0}".format(sp))
        pp, sp, mp = calculate_max_profit(sp)
        if mp > 0:
            print("\t Max profit {0} obtained when purchasing at {1} and selling at {2}".format(mp, pp, sp))
        else:
            print("\t No profit could be made :(")
