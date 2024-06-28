# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:34:10 2024

@author: Mugdha Shah
"""
#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading  the data
admissions_data = pd.read_csv('C:/Users/Mugdha Shah/Downloads/CollegeAdmissions_Data.csv')

# Displaying the first 5 rows of the data and the column names
admissions_data.head(), admissions_data.columns

# List unique university names to identify Ivy League schools
admissions_data['name'].unique()

# Filtering data to identify Ivy League Schools
ivy_league_schools = [
    "Brown University", "Columbia University in the City of New York", "Cornell University", 
    "Dartmouth College", "Harvard University", "Princeton University", 
    "University of Pennsylvania", "Yale University"
]

ivy_data = admissions_data[admissions_data['name'].isin(ivy_league_schools)]

# Group by parental income label and average the attendance rates
ivy_income_attendance = ivy_data.groupby('par_income_lab').agg({
    'attend': 'mean',
    'attend_sat': 'mean'
}).reset_index()

ivy_income_attendance


# Creating the plot
plt.figure(figsize=(20, 12))

# Plotting the general attendance rate
plt.plot(ivy_income_attendance['par_income_lab'], ivy_income_attendance['attend'], label='General Attendance Rate', marker='o')

# Plotting the attendance rate adjusted for SAT scores
plt.plot(ivy_income_attendance['par_income_lab'], ivy_income_attendance['attend_sat'], label='Attendance Rate Adjusted for SAT', marker='x')

# Adding titles and labels
#plt.title('Impact of Family Income on Ivy League School Attendance Rates', fontsize=16)
plt.xlabel('Parental Income Percentile', fontsize=22)
plt.ylabel('Average Attendance Rate', fontsize=22)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()

#the title, additional annotations and the text to explain blue and orange lines were added using Microsoft Powerpoint presentation.
