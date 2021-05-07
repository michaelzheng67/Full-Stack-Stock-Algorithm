# Full-Stack-Stock-Algorithm

Full stack trading app that mainly uses Python to co-ordinate stock trading decisions. Created with inspiration and tutorial sessions from github.com/hackingthemarkets and their full stack trading app. Their original trading strategy had been to include both long and short day trading strategies. However, my version of the trading app is configured to have only one long strategy, that being the opening range breakout. The selecting of stocks to use the strategy on is also automated, as we will take those that have been identified as "pre-market gappers" and automatically insert them into our strategy database to be traded with throughout the day. The basic functionality was taken from the tutorial sessions, however, the pregapper screening and automatic trading on preselected stocks, along with a large portion of the UI design, was my original work.  

Connects to Alpaca API to extract equity prices and execute trades to paper account. Algorithm utilizes database (Sqlite) which is continuously updated using cronjobs from terminal. 

Comes with UX/UI component where user is able to display localhost site by entering: uvicorn main app: --reload into terminal.

Example of this app working: Amazon stock has gapped up 5% in premarket trading and has opened 5% higher compared to the last trading day's close price. The stock algorithm will detect this and add Amazon stock to the table of equities that will be traded today. We will wait to see the price movement of the stock in the first couple minutes of open to establish a price range. Then, we will send an order for when the stock is looking to breakout and sell at predetermined price. 

Notes:

- When code is referring to the config file, that is simply a file of variables given to hide sensitive information (e.g alpaca api key password)
- The template and database within the app is reusable, thus, you can take out the opening_range_breakout.py file and replace it with whatever trade algorithm you need
- Make sure that you have some sort of way to continuously update the stocks table and stock prices. Personally, I used cronjobs within my computer's terminal in order to set whenever the stocks and stock prices .py files should run in order to update the data
- I don't have a list of what imports you need to make, but that can mostly be figured out from the very beginning of every file where I list all the imports
- You may have noticed that there is a table dedicated to strategies within the database schema. This was how the original tutorial designed the applcation. However, I'm only using one strategy to trade, so this table is obsolete for my specific use. However, the good thing is that it makes the schema reusable and scalable, so in case you wanted to design a multi-strategy application, it will be much easier to implement with a strategies table 
- This app is meant to connect to an Alpaca Trading Account 
