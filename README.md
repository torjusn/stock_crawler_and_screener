# Capital Stock Crawler and Screener
![frontpage](images/frontpage.png)

## Introduction
A stock screener uses a set of metrics to decide on which companies to invest in to predict the best possible return on investments. The screener this project is based on is called `Option 2: General Screening Instructions` and is an extended generalization of the main algorithm of the book `The Little Book That Beats the Market` by Joel Greenblatt that can be used without the books dedicated [stock screener website](https://www.magicformulainvesting.com/).

The philosophy behind this screener is to find a set of companies that on average trades at a bargain price relative to their true value. This is done with a margin of safety as the companies generally earn well compared to their cost with little debt and is further improved by spreading the portfolio over 20-30 stocks over a year. It is not only interested in the companies with the current greatest earnings to investment ratio but also companies that are good in the sense that they likely grow over time.

Crawling is the process of obtaining the metrics needed to perform a prediction algoriithm. This can be done by API for publically available financial sites such as Morningstar or Yahoo finance. In this project we will be using Python for both the screener and the crawler parts.

## Vanilla Screening Algorithm
- Use return on assets (ROA) as a screening criterion. Set the minimum ROA at 25%. (This will take the place of return on captial from the magic formula study.)
- From the resulting group of high ROA stocks, screen for thos estocks with the lowest price/earning (P/E) ratios. (This will take the place of earnings yield from the magic formula study.)
- Eliminate all utilities and financial stocks (i.e., mutual funds, banks, and insurance companies) from the list.
- Eliminate all foregin companies from the list. In most cases these will have the suffix "ADR" (for "American Depository Recepeit") after the name of the stock.
- If a stock has a very low P/E ratio, say 5 or less, that may indicate that the previous year or the data being used are unusual in some way. You may want to eliminate these stocks from your list. You may also want to eliminate any company that has announced earnings in the last week. (This should help minimize the incidence of incorrect or untimely data.)
- After obtaining your list, follow steps 4 and 8 from the magicformulainvesting.com instructrions.

Summarized Metrics needed:  
`ROA`, `P/E`, `company type`, `company nationality`.

## References
```
Greenblatt J. The Little Book That Still Beats the Market. 
Hoboken N.J: J. Wiley & Sons; 2010. http://site.ebrary.com/id/10419167. 
Accessed October 1 2022.
```

Special thanks to my colleague Thomas for giving me the opportunity to assist him in his stock adventures.
