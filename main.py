import csv
import random

# Function to generate color based on value
def get_color(value):
    if value <= 33:
        return 'green'
    elif value <= 66:
        return 'yellow'
    else:
        return 'red'

# Function to calculate efficiency percentage
def calculate_efficiency(output_work, input_work, time_lag, maximum_time_lag, efficiency_factor):
    efficiency = (output_work / input_work) * (1 - (time_lag / (maximum_time_lag * efficiency_factor))) * 100
    return efficiency

# Generate random data and write to CSV
output_work = 0
input_work = 0
time_lag_sum = 0
maximum_time_lag = 6
num_rows = 10
efficiency_factor = 10

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Random Value', 'Color', 'Time Lag'])

    for _ in range(num_rows):
        random_value = random.randint(1, 100)
        color = get_color(random_value)
        time_lag = round(random.uniform(1, 6), 2)
        output_work += random_value
        input_work += 100
        time_lag_sum += time_lag

        writer.writerow([random_value, color, time_lag])

# Calculate overall efficiency
average_time_lag = time_lag_sum / num_rows
overall_efficiency = calculate_efficiency(output_work, input_work, average_time_lag, maximum_time_lag, efficiency_factor)

print("Overall efficiency:", overall_efficiency, "%")