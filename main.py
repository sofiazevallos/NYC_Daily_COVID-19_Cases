#Name: Sofia Zevallos
#Email: sofia.zevallos75@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd 

f = input("Enter file name: ") 
cases = pd.read_csv(f) 

borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")
output = input("Enter output name: ")
column = cases[borough] 

print("Max: ", round(column.max(),3))
print("Min: ", round(column.min(),3))
print("Mean: ", round(column.mean(),3))
print("Median: ", round(column.median(),3))
print("Standard Deviation: ", round(column.std(),3)) 
 
cases['Fraction'] = column / cases['case_count']
cases.plot(x='date_of_interest', y='Fraction')
fig = plt.gcf()
fig.savefig(output)
