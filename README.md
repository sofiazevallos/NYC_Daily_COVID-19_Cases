# NYC_Daily_COVID-19_Cases

NYC COVID-19 Data Analysis

This Python program analyzes COVID-19 data for New York City boroughs and generates a plot depicting the fraction of cases over time.

Instructions:

-Run the program.

-Enter the filename of the COVID-19 data in CSV format.

-Choose a NYC borough (Bronx, Brooklyn, Queens, Manhattan, or Staten Island).

-Specify an output filename for the generated plot.


Program Steps:

1. Data Input:

-Prompts the user to enter the filename of a CSV file containing COVID-19 data.
Reads the CSV file into a Pandas DataFrame.

2. Borough Selection:

-Prompts the user to choose a NYC borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island).
Output Specification:

-Asks the user to provide a name for the output plot file.

3. Data Analysis:

-Calculates and prints statistics for the selected borough, including max, min, mean, median, and standard deviation.

4. Fraction Calculation:

Creates a new DataFrame column ('Fraction') by dividing the selected borough's column by the 'case_count' column.

5. Plotting:

-Plots the 'Fraction' column against the 'date_of_interest' column.

6. Save Plot:

-Saves the generated plot with the specified output filename.


Requirements:

-Python 3.x

-Matplotlib

-Pandas
