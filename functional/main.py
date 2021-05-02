import sqlite3
import config
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import alpaca_trade_api as tradeapi


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# run in terminal: uvicorn main:app --reload
# localhost:8000 to access main slash
@app.get("/")
def index(request: Request):
    stock_filter = request.query_params.get('filter', False)

    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        select symbol, name, exchange, gap from stock
        join stock_strategy
        where stock.id = stock_strategy.stock_id
    """)

    rows = cursor.fetchall()

    return templates.TemplateResponse("index.html", {"request": request, "stocks": rows})


@app.get("/strategies")
def strategies(request: Request):
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM strategy
    """)

    strategies = cursor.fetchall()

    return templates.TemplateResponse("strategies.html", {"request": request, "strategies": strategies})


@app.get("/orders")
def orders(request: Request):
    api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.BASE_URL)

    orders = api.list_orders(status='all')

    return templates.TemplateResponse("orders.html", {"request": request, "orders": orders})


@app.get("/strategy/{strategy_id}")
def strategy(request: Request, strategy_id):
    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM strategy
        WHERE id = ?
    """, (strategy_id,))

    strategy = cursor.fetchone()

    cursor.execute("""
        SELECT symbol, name 
        FROM stock JOIN stock_strategy on stock_strategy.stock_id = stock.id
        WHERE strategy_id = ?
    """, (strategy_id,))

    stocks = cursor.fetchall()

    return templates.TemplateResponse("strategy.html", {"request": request, "stocks": stocks, "strategy": strategy})

