import pandas as pd


def load_nasdaq_codes(nasdaq_csv_filepath: str):

    # List of all nasdaq listed companies from csv
    # https://www.nasdaq.com/market-activity/stocks/screener

    nasdaq_df = pd.read_csv(nasdaq_csv_filepath)

    # Get all symbols of nasdaq listed companies
    nasdaq_codes = nasdaq_df["Symbol"]
    nasdaq_codes = nasdaq_codes.values.tolist()

    return nasdaq_codes


def get_batched_nasdaq_codes(nasdaq_codes: list[str], batch_size: int):

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


def read_from_db(dbname: str, dbuser: str, query: str):

    # Connect to an existing database
    with psycopg.connect(f"dbname={dbname} user={dbuser}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Query the database and obtain data as Python objects.
            cur.execute(query)
            data = cur.fetchall()

    return data


def get_screened_stocks(stock_df):
    return
