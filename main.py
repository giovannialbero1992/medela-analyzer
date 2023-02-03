import csv
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import sys
from datetime import datetime

volumes = []
trend = []
days = []
numdays = []

args = sys.argv[1:]
if len(args) != 1:
    print("Usage: python main.py <filename>")
    sys.exit(1)

with open(args[0], 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip header row
    # check if the row start with date
    for i, row in enumerate(csvreader):
        # Get values for the trend line analysis
        x_dates = datetime.strptime(row[0], '%d-%m-%Y')
        x_num = dates.date2num(x_dates)
        volume = float(row[4])

        # Add data to lists
        volumes.append(volume)
        days.append(x_dates)
        numdays.append(x_num)

        # Check for trend
        if i > 0:
            if volumes[-1] > volumes[-2]:
                trend.append('increasing')
            else:
                trend.append('decreasing')
        else:
            trend.append(None)

# Reverse the lists to make the first element the most recent
volumes = volumes[::-1]
days = days[::-1]
numdays = numdays[::-1]
trend = trend[::-1]

# Plot data
plt.scatter(days, volumes, None, None, edgecolor='none')

#calculate equation for trendline
z = np.polyfit(numdays, volumes, 4)
p = np.poly1d(z)

#add trendline to plot
plt.plot(days, p(numdays), 'r--')

plt.xlabel('Date')
plt.ylabel('Volume (ml)')
plt.show()
