import pandas as pd
from datetime import datetime, timedelta


second_file_path = "/Users/EIK/Downloads/Takachar-GPT-main/Feeding_Rate.xlsx"
df2 = pd.read_excel(second_file_path)

# Iterate through the rows and columns of the DataFrame
for index, row in df2.iterrows():
    for col in df2.columns:
        cell_value = row[col]
        if cell_value == "Cumulative kg consumed":
            # Print the row, column, and cell coordinates
            target_row = index + 1
            target_col = int(col[-1])
            break

# Specify the column and the starting row
column_index = target_col
starting_row = target_row

# All values under "Cumulative kg consumed" column in a list
kg_values = df2.iloc[starting_row:, column_index].tolist()

# return kg_values
