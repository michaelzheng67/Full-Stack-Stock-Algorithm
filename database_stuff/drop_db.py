# file that allows user to drop all database tables in order to restart database schema
# Only run this script if for some reason there is a need to delete the existing tables
import sqlite3, config

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute("""
    DROP TABLE stock_price
""")

cursor.execute("""
    DROP TABLE stock
""")

cursor.execute("""
    DROP TABLE stock_strategy
""")

cursor.execute("""
    DROP TABLE strategy
""")

connection.commit()
