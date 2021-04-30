import sqlite3
import config
import alpaca_trade_api as tradeapi
from datetime import date
from timezone import is_dst

api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.BASE_URL)
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

current_date = date.today().isoformat()

if is_dst():
    start_minute_bar = f"{current_date} 09:30:00-05:00"
    end_minute_bar = f"{current_date} 09:45:00-05:00"
else:
    start_minute_bar = f"{current_date} 09:30:00-04:00"
    end_minute_bar = f"{current_date} 09:45:00-04:00"


cursor.execute("""
    select stock.id, symbol, date, close from stock_price
    join stock
    on stock_price.id = stock.id
    where date = ?
""", (current_date,))

stocks = cursor.fetchall()
stock_dict = {}
symbols = []

for stock in stocks:
    minute_bars = api.get_barset(stock, '5Min', 85).df
    minute_bars.columns = ['open', 'high', 'low', 'close', 'volume']

    close_price = minute_bars.at_time('16:00')['close'].min()
    open_price = minute_bars.at_time('9:30')['open'].min()
    gap = ((open_price - close_price) / close_price) * 100
    # if the stock is identified as a premarket gapper
    # requirements to be gapper is 4%+ gap but that can be dynamically changed too
    if abs(gap) >= 4:
        symbol = stock['symbol']
        symbols.append(symbol)
        stock_dict[symbol] = stock['id']
        stock_id = stock_dict[symbol]

        cursor.execute("""
            insert into stock_strategy (stock_id, strategy_id)
            values (?, ?)
        """, (stock_id, 1))
        # hard coded breakout strategy id for insert statement but it can also be edited to be dynamic


connection.commit()
