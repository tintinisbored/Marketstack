
import requests
import pandas as pd

# Project variables
access_key = "19b60d7d53fe00f5b10afae773c8e61e"
eod_url = "https://api.marketstack.com/v1/eod"
symbol = "MSFT,AAPL,AMZN,GOOG,GOOGL"
limit = 1000
offset = 0 

# # Tickers endpoint and parameters
# tickers_url = "https://api.marketstack.com/v1/tickers"

# params_tickers = {
#     "access_key": access_key
# }

# # Make the GET request
# response_tickers = requests.get(tickers_url, params=params_tickers)

# Extract only the symbol from the JSON response to use it in the EOD params.
# tickers_data = response_tickers.json()['data']
# symbols = [item["symbol"] for item in tickers_data]
# symbols_comma = ",".join(symbols)

# EOD params
params_eod = {
    "access_key": access_key,
    "symbols": symbol,
    "limit": limit,
    "offset": offset
}

# Make the GET request to get all end of day data for all tickers
response_eod = requests.get(eod_url, params=params_eod)

# Create a pandas dataframe
eod_data = response_eod.json()
df = pd.DataFrame(eod_data['data'])

# Save df to CSV
df.to_csv('eod_data.csv', index=False)
