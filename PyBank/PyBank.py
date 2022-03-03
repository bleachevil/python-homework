import csv
import pprint
import numpy as np
from numpy import average

rows = []


file = open('budget_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
for row in csvreader:
    rows.append(row)

# split the list:
res1, res2 = map(list, zip(*rows))

# change string to int:
for i in range(0, len(res2)):
    res2[i] = int(res2[i])




print("Financial Analysis")
print("----------------------")
print(f'Total Months: {len(res1)}')
print(f'Total: {sum(res2)}')
print(f'Average Change: ${np.round(average(res2),2)}')
# search the greatest Increase from the original list:
Increase = max(res2)
for Great in rows:
    if str(Increase) in Great:
        print(f'Greatest Increase in Profits: {Great}')
        

# search the greatest Decrease from the original list:
Decrease = min(res2)
for low in rows:
    if str(Decrease) in low:
        print(f'Greatest Decrease in Profits: {low}')