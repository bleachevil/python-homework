import csv
import pprint
import numpy as np
from numpy import average
import pandas as pd

df = pd.read_csv('budget_data.csv')

total_month = len(df['Date'])
print(total_month)

total = sum(df['Profit/Losses'])

df['diff'] = df['Profit/Losses'].diff().fillna(0)

average_change = sum(df['diff']) / (total_month - 1)



print("Financial Analysis")
print("----------------------")
print(f'Total Months: {total_month}')
print(f'Total: ${total}')
print(f'Average Change: ${np.round(average_change,2)}')
# search the greatest Increase from the original list:
Great = df.loc[df['diff'] == max(df['diff'])]
#print(Great)
DateG= Great.iloc[0]['Date']
#print(DateG)
DiffG= Great.iloc[0]['diff']
#print(DiffG)
print(f'Greatest Increase in Profits: {DateG} (${DiffG})')
        

# search the greatest Decrease from the original list:
low = df.loc[df['diff'] == min(df['diff'])]
#print(low)
DateG= low.iloc[0]['Date']
#print(DateG)
DiffG= low.iloc[0]['diff']
#print(DiffG)
print(f'Greatest Decrease in Loss: {DateG} (${DiffG})')