import csv
import numpy as np
from numpy import average

rows = []
changes = []

file = open('budget_data.csv')
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
for row in csvreader:
    rows.append(row)
print(rows)

res1 = [i[1] for i in rows] 
res2 = [i[0] for i in rows]

#print(res1,res2)

for i in range(0, len(res1)):
    res1[i] = int(res1[i])

change = [y - x for x,y in zip(res1,res1[1:])]

max = max(change)
min = min(change)
    
#print(change)

print("Financial Analysis")
print("----------------------")
print(f'Total Months: {len(res2)}')
print(f'Total: ${sum(res1)}')
print(f'Average Change: ${np.round(average(change),2)}')
# search the greatest Increase from the original list:

for x in range(0,len(change)):
    if change[x] == max:
        #print(x)
        dated = res2[x+1]
        amounted = np.around(change[x],0)
    
        print(f'Greatest Increase in Profits: {dated} (${amounted})')
        

# search the greatest Decrease from the original list:
for x in range(0,len(change)):
    if change[x] == min:
        #print(x)
        dated = res2[x+1]
        amounted = np.around(change[x],0)
    
        print(f'Greatest Decrease in Loss: {dated} (${amounted})')