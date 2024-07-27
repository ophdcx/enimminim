import json
import pandas as pd

# Load the JSON list into pandas dataframe
json_data = '[{"code": "A", "value": 10}, {"code": "B", "value": 20}, {"code": "A", "value": 30}]'
df = pd.read_json(json_data)

# Group the pandas dataframe by code
grouped_df = df.groupby('code').sum()

# Save the pandas dataframe as html table to /tmp/ directory
grouped_df.to_html('/tmp/grouped_data.html')
