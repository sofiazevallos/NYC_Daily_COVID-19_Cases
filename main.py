#Name: Sofia Zevallos
#Email: sofia.zevallos75@myhunter.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd 

f = input("Enter file name: ") //Prompts the user to enter a file name and stores that input in the variable f. 
cases = pd.read_csv(f) //Reads a CSV file specified by the user (through the input obtained in the previous line) and stores it in a Pandas DataFrame called cases. 

borough = input("Enter borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island): ")//Prompts the user to enter a borough name (Bronx, Brooklyn, Queens, Manhattan, or Staten Island) and stores the input in the variable borough.
output = input("Enter output name: ") //Prompts the user to enter an output name and stores the input in the variable output.
column = cases[borough] //Extracts the column corresponding to the borough entered by the user and stores it in the variable column. 

//The following lines print statistics about the selected column

print("Max: ", round(column.max(),3)) //Prints the maximum value in the column rounded to 3 decimal places.
print("Min: ", round(column.min(),3)) //Prints the minimum value in the column rounded to 3 decimal places.
print("Mean: ", round(column.mean(),3)) //Prints the average value of the column rounded to 3 decimal places.
print("Median: ", round(column.median(),3)) //Prints the median value of the column rounded to 3 decimal places.
print("Standard Deviation: ", round(column.std(),3)) //Prints the standard deviation of the column rounded to 3 decimal places.
 
cases['Fraction'] = column / cases['case_count'] //Creates a new column in the DataFrame called 'Fraction', which contains the values obtained by dividing the previously selected column by the 'case_count' column.
cases.plot(x='date_of_interest', y='Fraction') //Plots a graph using the DataFrame. The x-axis is specified as the 'date_of_interest' column, and the y-axis is specified as the 'Fraction' column.
fig = plt.gcf() //Gets the current figure from the matplotlib library.
fig.savefig(output) //Saves the current figure (the plot) to a file with the name specified by the user in the output variable. The file format is determined by the extension of the output name (e.g., '.png' for a PNG file).
