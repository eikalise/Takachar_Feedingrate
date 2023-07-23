import pandas as pd
from datetime import datetime

from cumulative_kg_consumed import kg_values
from return_time_feed import time_feed, data_dict
from return_time_N import time_N

    # Define the two time points
    #time1 = datetime.strptime('10:30:00', '%H:%M:%S')
   # time2 = datetime.strptime('14:45:30', '%H:%M:%S')

df = pd.read_excel('/Users/EIK/Downloads/Takachar-GPT-main/NSTPROR00006-2023-06-22 (1).xlsx')

# Find the time difference for each pair of times
time_feed_new = [datetime.strptime(time, "%H:%M").strftime("%H:%M:%S") for time in time_feed]

time_feed_dt = [datetime.strptime(time, "%H:%M:%S") for time in time_feed_new]
time_N_dt = [datetime.strptime(time, "%H:%M:%S") for time in time_N]

for i, N_time in enumerate(time_N_dt):
    smallest_diff = None
    smallest_diff_index_feed = None

    # Iterate over each time_feed element
    for j, feed_time in enumerate(time_feed_dt):
        # Calculate time difference
        diff = abs(N_time - feed_time)

        # Update smallest difference and index if it is the smallest encountered so far
        if smallest_diff is None or diff < smallest_diff:
            smallest_diff = diff
            smallest_diff_index_feed = j

    # Get the corresponding time_feed and combustion kg based on the smallest time difference
    closest_feed_time = time_feed[smallest_diff_index_feed]
    cumulative_kg = data_dict[closest_feed_time]

    # Update the corresponding row in the DataFrame with the combustion kg value
    df.at[i, 'Cumulative kg'] = cumulative_kg

# Save the updated DataFrame to a new Excel file
df.to_excel('/Users/EIK/Downloads/Takachar-GPT-main/NSTPROR00006-2023-06-22 (1).xlsx', index=False)

