# Full-Stack-Stock-Algorithm

Full stack trading app that mainly uses Python to co-ordinate stock trading decisions. Created with inspiration from github.com/hackingthemarkets and their full stack trading app. Their original trading strategy had been to include both long and short day trading strategies. However, my version of the trading app is configured to have only one long strategy, that being the opening range breakout. The selecting of stocks to use the strategy on is also automated, as we will take those that have been identified as "pre-market gappers" and automatically insert them into our strategy database to be traded with throughout the day. 

Connects to Alpaca API to extract equity prices and execute trades to paper account. Algorithm utilizes database (Sqlite) which is continuously updated using cronjobs from terminal. 

Comes with UX/UI component where user is able to display localhost site by entering: uvicorn main app: --reload into terminal.

Notes:

- When code is referring to the config file, that is simply a file of variables given to hide sensitive information (e.g alpaca api key password)
