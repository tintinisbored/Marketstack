
import requests
import pandas as pd

# Project variables
access_key = "19b60d7d53fe00f5b10afae773c8e61e"
tickers_url = "https://api.marketstack.com/v1/tickers"
limit = 5

# API endpoint and parameters

params = {
    'limit': limit,
    'access_key': access_key  # Replace with your actual access key
}

# Make the GET request
response = requests.get(tickers_url, params=params)

# Create a pandas dataframe
data_dic = response.json()['data']

flattened_data = []
for item in data_dic:
    flattened_item = item.copy()
    stock_exchange = flattened_item.pop("stock_exchange")
    # Add stock_exchange fields to the main dictionary
    for key, value in stock_exchange.items():
        flattened_item[f"stock_exchange_{key}"] = value
    flattened_data.append(flattened_item)

# Convert to DataFrame
df = pd.DataFrame(flattened_data)

# Display the result
print(df)


