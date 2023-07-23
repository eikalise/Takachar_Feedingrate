import pandas as pd
from datetime import datetime

# Read the Excel file into a DataFrame
df = pd.read_excel('/Users/EIK/Downloads/Takachar-GPT-main/NSTPROR00006-2023-06-22 (1).xlsx')

# Specify the column name containing the timestamp data
timestamp_column = 'Time'

# Extract the timestamp data column
timestamp_data = df[timestamp_column].tolist()

# Print the timestamp data
time_N = []
for timestamp in timestamp_data:
    datetime_obj = datetime.strptime(timestamp, '%I:%M:%S %p')
    time_str = datetime_obj.strftime('%H:%M:%S')
    time_N.append(time_str)
#Return time_N
print(time_N)

