
import requests
import pandas as pd

# Project variables
access_key = "19b60d7d53fe00f5b10afae773c8e61e"
div_url = "https://api.marketstack.com/v1/dividends"
symbol = "MSFT,AAPL,AMZN,GOOG,GOOGL"
limit = 1000
offset = 0 


# Dividends params
params_div = {
    "access_key": access_key,
    "symbols": symbol,
    "limit": limit,
    "offset": offset
}

# Make the GET request to get all end of day data for all tickers
response_eod = requests.get(div_url, params=params_div)

# Create a pandas dataframe
eod_data = response_eod.json()
df = pd.DataFrame(eod_data['data'])

# Save df to CSV
df.to_csv('dividends.csv', index=False)
