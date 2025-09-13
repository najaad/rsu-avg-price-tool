from datetime import datetime, timedelta
import math
import yfinance as yf

# TODO - Update to be CLI friendly 

# User Configured values
COMPANY_TICKER = "MSFT"
GRANT_DATE = "2025-08-15"
DAYS_IN_RANGE = 30
RSU_GRANT = 500000


def get_start_date(grant_date: str, days_in_range: int) -> str:
   """Return the start date string for averaging stock prices."""
   date_format = "%Y-%m-%d"
   dt_object = datetime.strptime(grant_date, date_format)
   start_dt = dt_object - timedelta(days=days_in_range)
   return start_dt.strftime(date_format)

def main():
   ticker = yf.Ticker(COMPANY_TICKER)
   start_range = get_start_date(GRANT_DATE, DAYS_IN_RANGE)
   history = ticker.history(start=start_range, end=GRANT_DATE)

   price_data = history.drop(columns=["Dividends", "Volume", "Stock Splits"])
   avg_close_price = round(price_data["Close"].mean(), 2)

   print(f"Grant Date: {GRANT_DATE}")
   print(f"Avg Close Price: {avg_close_price}")

   whole_shares = math.floor(RSU_GRANT / avg_close_price)
   print(f"Whole Shares Awarded: {whole_shares}")

   fractional_shares = RSU_GRANT / avg_close_price
   print(f"Fractional Shares Awarded: {fractional_shares}")


if __name__ == "__main__":
   main()