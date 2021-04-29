# calculate the quantity of stocks that we want to buy as a proportion of our trading account size (hard coded for now)
import math


def calculate_quantity(price):
    quantity = math.floor(10000 / price)

    return quantity
