import pandas as pd
from datetime import datetime, timedelta
from cumulative_kg_consumed import kg_values

# Read the Excel file into a DataFrame
df = pd.read_excel('/Users/EIK/Downloads/Takachar-GPT-main/Feeding_Rate.xlsx')

# Find the column index for the "Timestamp" header
for index, row in df.iterrows():
    for col_index, col in enumerate(df.columns):
        cell_value = row[col_index]
        if cell_value == "Timestamp (hh:mm format)":

            # Print the row, column, and cell coordinates
            target_row = index + 1
            target_col = col_index
            break

# Specify the column and the starting row
column_index = target_col
starting_row = target_row

# All values under "Cumulative kg consumed" column in a list
values = df.iloc[starting_row:, column_index].tolist()
time_feed = []

for i in values:
    try:
        formatted_time = i.strftime("%H:%M")
        time_feed.append(formatted_time)
    except:
        continue

#return time_feed
print(time_feed)

# Create a dictionary with time as keys and kg as values
data_dict = dict(zip(time_feed, kg_values))
#return data_dict
