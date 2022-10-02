# -----------------------------------------------------------
# company stock crawler and screener
#
# Torjus Nilsen, Drammen, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

import yfinance as yf
import finnhub

"""
TODO
[ ] Loop through all relevant NASDAQ listed company codes
[ ] create requirements.txt file
[ ] create crawler for relevant metrics
[ ] apply screening algorithm
"""

msft = yf.Ticker("MSFT")

# get stock info
# print(msft.info.keys())
recommendations = msft.recommendations

# info includes return on assets, trailingEps (Price to earnings)
info = msft.info()

# financials includes net income
financials = msft.get_financials()


print(financials)
exit()

occur = recommendations.groupby(["To Grade"]).size()
print(occur)
exit()
