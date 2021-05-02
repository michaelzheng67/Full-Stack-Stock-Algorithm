# Keep databases updated with new information during the trading days and times by initiating cronjobs within terminal to keep the corresponding scripts running and log activity to log file 

0 22 * * * <Location path within computer for python environment> /Users/michaelzheng/Projects/algo-trading/populate_db.py >> populate.log 2>&1

*/5 9-16 * * 1-5 <Location path within computer for python environment> /Users/michaelzheng/Projects/algo-trading/opening_range_breakout.py >> trade.log 2>&1

35 9 * * 1-5 <Location path within computer for python environment> /Users/michaelzheng/Projects/algo-trading/premarket_gappers.py >> gappers.log 2>&1
