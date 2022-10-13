# -----------------------------------------------------------
# nasdaq stock crawler and screener
#
# Torjus Nilsen, Drammen, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

# standard lib
import time
import logging
from pathlib import Path

# finance api
import yfinance as yf

# data
import pandas as pd

# database
import psycopg

"""
TODO
fjern
\i C:/Users/torni/git/stock_crawler_and_screener/src/sql/create_db_schemas_tables.sql
-[ ] authenticate API key for more requests? https://stackoverflow.com/questions/9346582/what-is-the-query-limit-on-yahoos-finance-api
"""

#
# The goal of this script is to:
# - read all nasdaq listed companies from csv
# - extract financial data on possible nasdaq listed stocks from yfinance python api
# - perform screening alg to select interesting stocks from all nasdaq stocks
#
# For a general introduction on extracting stock data with yfinance see
# https://analyzingalpha.com/yfinance-python
#

FILE_DIR = Path(__file__).parent
DATA_DIR = FILE_DIR / "data"

# list of all nasdaq listed companies from csv
# https://www.nasdaq.com/market-activity/stocks/screener
nasdaq_path = DATA_DIR / "nasdaq_screener_1665505677186.csv"
nasdaq_df = pd.read_csv(nasdaq_path)

# get all symbols of nasdaq listed companies
nasdaq_symbols = nasdaq_df["Symbol"]
nasdaq_symbols = nasdaq_symbols.values.tolist()


def get_nasdaq_stocklist():
    stocks = 1
    return stocks


def main():

    step = 1999

    for batch_idx in range(0, len(nasdaq_symbols), step):
        current_nasdaq_symbols = nasdaq_symbols[batch_idx : (batch_idx + step)]

    # yahoo finance free public API is limited to 2.000 requests per hour per IP adress
    # loop through 1999 ~hour until stack is emptied.
    stock_ticker = yf.Ticker("AAPL", "GOOG")

    info_dict = stock_ticker.info

    # info includes return on assets, trailingEps (Price to earnings)
    info_dict = stock_ticker.info
    keys = ["returnOnAssets", "fullTimeEmployees"]
    for key in keys:
        test = info_dict[key]
        print(test)
    # return_on_assets =
    # print(return_on_assets)

    price_to_earnings_ratio = info_dict["trailingEps"]

    # financials includes net income
    # financials_df = stock_ticker.get_financials()
    # get first element, i.e. most recent quarters net income
    # net_income = financials_df.loc["Net Income"][0]
    return


if __name__ == "__main__":
    main()
"""
TODO
[ ] Logger and logfile
[ ] Move screener to separate script, only pipe data here
[ ] Loop through all relevant NASDAQ listed company codes
[ ] create requirements.txt file
[ ] create crawler for relevant metrics
[ ] apply screening algorithm
"""
