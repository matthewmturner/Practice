import math


def get_max_profit(stock_prices):

    max_profit = None

    for i, px in enumerate(stock_prices):
        if i == 0:
            low_price = px
        elif i == 1:
            max_profit = px - low_price
            if px < low_price:
                low_price = px
        else:
            profit = px - low_price
            if profit > max_profit:
                max_profit = profit
                if px < low_price:
                    low_price = px
            elif px < low_price:
                low_price = px

    return max_profit


p = [10, 7, 6, 5, 3, 2]
print(get_max_profit(p))
