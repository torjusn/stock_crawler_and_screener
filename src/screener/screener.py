# -----------------------------------------------------------
# nasdaq stock crawler and screener
#
# Torjus Nilsen, Drammen, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

# standard lib
import argparse
import time
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# finance api
import yfinance as yf

# data
import pandas as pd

# database
import psycopg

# local
from functions import (
    load_nasdaq_codes,
    get_batched_nasdaq_codes,
    write_to_db,
    get_screened_stocks,
)

parser = argparse.ArgumentParser(description="Screen and save stocks to DB")

# run options
parser.add_argument(
    "--save-to-db",
    action=argparse.BooleanOptionalAction,
    help="avoid saving new stocks to db without meaning to",
)

# hyperparams
parser.add_argument(
    "--stocks-per-screening",
    default=1999,
    type=int,
    metavar="",
    help="limit stocks screened per batch as yfinance cap number of requests per hour per ip",
)

args = parser.parse_args()

# logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger.setLevel(logging.INFO)

# add a rotating handler, i.e. overwrite earliest first if log is full
logger_path = Path(__file__).stem + ".log"
handler = RotatingFileHandler(logger_path, maxBytes=50000, backupCount=5)
logger.addHandler(handler)
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(log_formatter)

"""
try:
    swag()
except:
    logger.exception("wtf")
"""

"""
TODO
[ ] add pydantic + .env files
[ ] create requirements.txt file
[ ] add typehints
[x] create crawler for relevant metrics
[ ] apply screening algorithm
"""

"""
fjern
\i C:/Users/torni/git/stock_crawler_and_screener/src/sql/create_db_schemas_tables.sql
-[ ] authenticate API key for more requests? https://stackoverflow.com/questions/9346582/what-is-the-query-limit-on-yahoos-finance-api
"""

#
# The goal of this script is to:
# - read codes of all nasdaq listed companies from csv
# - extract financial data on possible nasdaq listed stocks from yfinance python api
# - perform screening alg to select interesting stocks from all nasdaq stocks
#
# For a general introduction on extracting stock data with yfinance see
# https://analyzingalpha.com/yfinance-python
#

FILE_DIR = Path(__file__).parent
DATA_DIR = FILE_DIR / "data"

DBNAME = "stocks"
DBUSER = "postgres"
NASDAQ_CSV_FILENAME = "nasdaq_screener_1665505677186.csv"


def get_write_query(nasdaq_code, company_name, selection_date):

    query = """
    INSERT INTO metadata.tracked_stocks
    VALUES 
        ();
    """

    return query


# TODO move to other script
def get_read_query():
    """
    query function for order
    """
    query = """SELECT * FROM metadata.tracked_stocks"""

    return query


def main():

    logger.info(f"Started Script: save_to_db [{args.save_to_db}]")

    nasdaq_csv_filepath = DATA_DIR / NASDAQ_CSV_FILENAME
    nasdaq_codes = load_nasdaq_codes(nasdaq_csv_filepath)
    nasdaq_codes_batched = get_batched_nasdaq_codes(
        nasdaq_codes, args.stocks_per_screening
    )

    logger.info(
        f"Screening [{len(nasdaq_codes)}] stocks in [{len(nasdaq_codes_batched)}] batches"
    )

    for batch_idx, current_nasdaq_codes in enumerate(nasdaq_codes_batched):
        print(codes)
        print(len(codes))

        # TODO uncomment
        # wait one hour
        # time.sleep(3600 + 1)
        exit()

    get_screened_stocks(stock_df)

    logger.info("Finished Script")

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

    if args.save_to_db:
        write_query = get_write_query()
        write_to_db(write_query)
        print("hade")

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

