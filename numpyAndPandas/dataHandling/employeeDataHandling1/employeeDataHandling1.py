import numpy as np
import pandas as pd

# Converting dataframe to a 2D numpy array...
myDataFrame = pd.read_csv('employees1.csv')
data = myDataFrame.to_numpy()

print("\nEMPLOYEE DATA HANDLING RESULTS")
print("====================================")
# YOUNGEST EMPLOYEE
ages = data[:, 2]
minimumAge = min(ages)
isMinimum = (ages == minimumAge)
# isMinimum is an array of Boolean elements
# (corresponding to whether a the age is the minimum age)

# Obtaining the record of the employee(s) with the minimum age...
employeesWithMinimumAge = data[isMinimum]
print("The employee(s) with the minimum age have the following details:")
print("-- Columns:", myDataFrame.columns.values, "--")
print(employeesWithMinimumAge)
print("====================================")
# MOST EXPERIENCED EMPLOYEE
xp = data[:, 3]
maximumExperience = max(xp)
isMaximum = (xp == maximumExperience)
# isMaximum is an array of Boolean elements
# (corresponding to whether a the experience is the maximum)

# Obtaining the record of the employee(s) with the minimum age...
employeesWithMaximumXp = data[isMaximum]
print("The employee(s) with the maximum experience have the following details:")
print("-- Columns:", myDataFrame.columns.values, "--")
print(employeesWithMaximumXp)
print("====================================")
# AVERAGE SALARY OF EMPLOYEES BETWEEN AGES 30 AND 40
ages = data[:, 2]
isWithinGivenRange = (ages > 30) & (ages < 40)
# isWithinGivenRange is an array of Boolean elements
# (corresponding to whether a the age is bewteen 30 and 40)
salaries = data[:, 1]
salariesForAgesWithinGivenRange = salaries[isWithinGivenRange]

# The average of the obtained values...
print("Mean salary of employees of ages between 30 and 40 is", end = " ")
print(np.mean(salariesForAgesWithinGivenRange))
print("\n")