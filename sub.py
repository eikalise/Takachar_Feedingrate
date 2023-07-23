
from datetime import datetime

numbers=['11:15', '11:21', '11:24', '11:42', '11:45', '11:50', '11:55', '12:02', '12:10', '12:17', '12:25',
           '12:31', '12:40', '12:45', '12:51', '13:19', '13:25', '13:30', '13:52', '13:58', '14:04', '14:08',
           '14:22', '14:24', '14:27', '14:35', '14:51', '14:56', '15:00', '15:10', '15:35', '15:44', '15:49',
           '15:54', '16:14']
datetime_objects = [datetime.strptime(numbers[0], '%H:%M:%S'), datetime.strptime(numbers[1], '%H:%M:%S')]

# Convert the remaining elements and format them in the same way
for number in numbers[2:]:
    # Convert to datetime object
    datetime_obj = datetime.strptime(number, '%H:%M')

    # Format as string in desired format
    formatted_number = datetime_obj.strftime('%H:%M:%S')

    # Append to the list of datetime objects
    datetime_objects.append(formatted_number)

print(datetime_objects)

