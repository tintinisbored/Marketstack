

import requests
import pandas as pd

# Project variables
access_key = "19b60d7d53fe00f5b10afae773c8e61e"
exchanges_url = 'https://api.marketstack.com/v1/exchanges'
limit = 100

# API endpoint and parameters

params = {
    'limit': limit,
    'access_key': access_key  # Replace with your actual access key
}

# Make the GET request
response = requests.get(exchanges_url, params=params)

# Create a pandas dataframe
data_dic = response.json()['data']

flattened_data = []
for item in data_dic:
    flattened_item = item.copy()  # Copy the original item
    # Flatten the nested dictionaries dynamically
    for key in ["timezone", "currency"]:
        nested_data = flattened_item.pop(key)  # Remove and get the nested dictionary
        for nested_key, nested_value in nested_data.items():
            flattened_item[f"{key}_{nested_key}"] = nested_value  # Add flattened fields
    flattened_data.append(flattened_item)

# Convert to a pandas DataFrame for easier viewing or manipulation
df = pd.DataFrame(flattened_data)

# Save data to CSV file
df.to_csv('exchanges.csv', index=False)


