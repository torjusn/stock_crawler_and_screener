import pandas as pd
from pandas_datareader import data as pdr

# finance api
import yfinance as yf


def load_nasdaq_codes(nasdaq_csv_filepath: str) -> list[str]:

    # List of all nasdaq listed companies from csv
    # https://www.nasdaq.com/market-activity/stocks/screener

    nasdaq_df = pd.read_csv(nasdaq_csv_filepath)

    # Get all symbols of nasdaq listed companies
    nasdaq_codes = nasdaq_df["Symbol"]
    nasdaq_codes = nasdaq_codes.values.tolist()

    return nasdaq_codes


def get_batched_nasdaq_codes(nasdaq_codes: list[str], batch_size: int) -> list:

    batched_nasdaq_codes = []

    for batch_idx in range(0, len(nasdaq_codes), batch_size):
        current_nasdaq_codes = nasdaq_codes[batch_idx : (batch_idx + batch_size)]
        batched_nasdaq_codes.append(current_nasdaq_codes)

    return batched_nasdaq_codes


def write_to_db(dbname: str, dbuser: str, query: str):

    # Connect to an existing database
    with psycopg.connect(f"dbname={dbname} user={dbuser}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Execute a command
            cur.execute(query)

            # Make the changes to the database persistent
            conn.commit()


# TODO return typehint
def read_from_db(dbname: str, dbuser: str, query: str):

    # Connect to an existing database
    with psycopg.connect(f"dbname={dbname} user={dbuser}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Query the database and obtain data as Python objects.
            cur.execute(query)
            data = cur.fetchall()

    return data


def load_one_stock_data(nasdaq_code: str):
    """
    Helper Function not in use. 
    Saved for future reference on using only one (1) stock/ticker.
    """

    # nasdaq_code = "AAPL" # apple inc
    stock_ticker = yf.Ticker(nasdaq_code)
    info_dict = stock_ticker.info

    # info includes return on assets, trailingEps (Price to earnings)
    info_dict = stock_ticker.info
    keys = ["returnOnAssets", "fullTimeEmployees"]

    price_to_earnings_ratio = info_dict["trailingEps"]

    # financials includes net income
    financials_df = stock_ticker.get_financials()
    # get first element, i.e. most recent quarters net income
    net_income = financials_df.loc["Net Income"][0]

    return info_dict, financials_df


def load_stock_data(nasdaq_codes: list[str]):
    """
    This function takes in a list of nasdaq codes, e.g. google and apple = ["GOOG", "AAPL"]  and uses it to download
    relevant recent financial data used in screening. This can be done in multiple ways:
    - Option 1: Using yfinance .download() method.
    - Option 2 (recommended): Using outside library pandas_datareader with pdr_override() as recommended by the creator
        of yfinance.
    """

    ###
    # OPTION 1: YAHOO FINANCE DOWNLOAD METHOD
    ###

    # yfinance download method instead of using multiple tickers
    # data = yf.download(nasdaq_codes, start="2017-01-01", end="2017-04-30")
    exit()
    ###
    # OPTION 2 (recommmended): PANDAS DATAREADER
    ###

    # pandas datareader library
    # https://stackoverflow.com/questions/49705047/downloading-mutliple-stocks-at-once-from-yahoo-finance-python
    # df = pdr.DataReader(tickers, data_source='yahoo', start='2017-01-01', end='2020-09-28') # tickers = ['msft', 'aapl']

    """
    If your code uses pandas_datareader and you want to download data faster, you can "hijack" 
    pandas_datareader.data.get_data_yahoo() method to use yfinance while making sure the returned data is in the same 
    format as pandas_datareader's get_data_yahoo().
    """

    yf.pdr_override()  # <== that's all it takes :-)
    df = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")
    print(df.columns)
    print(df.head)
    exit()

    return info_dict


def get_screened_stocks(stock_df):
    return
