# calculate the quantity of stocks that we want to buy as a proportion of our trading account size 
import math
import alpaca_trade_api as tradeapi
import config

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.BASE_URL)
account = api.get_account()
total_amount = account.buying_power

# We will risk 5% of buying power in each transaction
def calculate_quantity(price):
    quantity = math.floor( (total_amount * 0.05) / price)
    return quantity
