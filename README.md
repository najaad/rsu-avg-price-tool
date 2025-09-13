# ⭐ RSU Grant Stock Price Analyzer

This Python script uses `yfinance` [(GH Repo)](https://github.com/ranaroussi/yfinance) to calculate the average closing price of a stock over a specified number of days leading up to a RSU (Restricted Stock Unit) grant date. It then calculates the number of whole and fractional shares granted based on a total RSU dollar amount.

## ⭐ What It Does

* Fetches historical stock data using `yfinance`
* Calculates the average closing price over a user-defined number of days before the grant date
* Computes how many **whole** and **fractional** shares are awarded based on a fixed RSU grant value

## ⭐ How to Use

1. Update the following values at the top of the script:

   ```python
   COMPANY_TICKER = "MSFT"       # Stock symbol
   GRANT_DATE = "2025-08-15"     # RSU grant date (YYYY-MM-DD)
   DAYS_IN_RANGE = 30            # Number of days before grant date to average
   RSU_GRANT = 500000            # Dollar value of RSU grant
   ```

2. Run the script.

3. Output will show:

   * Grant Date
   * 30-Day Average Close Price
   * Whole Shares Awarded
   * Fractional Shares Awarded

## ⭐ Requirements

Install required packages:

```bash
pip3 install yfinance pandas
```