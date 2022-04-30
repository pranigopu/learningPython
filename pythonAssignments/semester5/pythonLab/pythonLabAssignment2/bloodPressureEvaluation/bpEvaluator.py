# Write a python program to store the blood pressure test values of 10 patients.
# Store the values in a dictionary (Systolic, Diastolic).
# From the observation results, propose the stage of blood pressure they are in.

from os.path import isfile
from bpDataProcessing import bpStage, processData

# IMPORTANT VARIABLES
dataFileName = "patientData.txt"
processedData = []
original = {}   # Empty dictionary or set... Dictionary in this case
results = {}    # Empty dictionary or set... Dictionary in this case
dataFile = "*"
dataFileHeaderCount = 1

# CHECKING IF DATA FILE EXISTS
if isfile(dataFileName):
    dataFile = open(dataFileName, "r") # Opening the file stream.
    # "r" mode is default. If no mode argument were passed, it would default to "r".
else:
    print("\nData file '" + dataFileName + "' not found.\n")
    exit() # Terminates main program.

# ENTERING THE STARTING LINE TO READ THE FILE FROM
print("\nPATIENT BLOOD PRESSURE DATA RESULTS\n")
try:
    start = int(input("Start reading from line... ")) - 1 + dataFileHeaderCount
    # We are dealing with lines by making a list of them.
    # Hence, the 1st line will be at index 0.
    # Hence, we subtract the inputted line number by 1.
    # We then add to it the number of header lines expected in the file.
    # Hence, if we input 1, we start at the 1st data line.
except:
    print("\nInvalid starting line. Defaulting to", dataFileHeaderCount, end = ".\n")
    start =  dataFileHeaderCount
    # Again accounting for the fact that the 1st index is 0, and there are "dataFileHeaderCount" expected header lines.

# STORING THE SPECIFIED 10 LINES OF THE FILE
lines = dataFile.readlines()[start : start + 10]
# There is no error if the upper bound exceeds the number of lines.
# Hence, "lines" will store less than or equal to 10 lines.

print()
for line in lines:
    # PROCESSING THE LINE INTO A VALIDATED LIST
    processedData = processData(line)
    if processedData == []:
        print("Error in reading file!")
        break
    # CREATING DICTIONARIES
    name = processedData[0]
    systolic = processedData[1]
    diastolic = processedData[2]
    original[name] = [systolic, diastolic]
    results[name] = bpStage(systolic, diastolic)

dataFile.close() # Closing the file stream.

# FINAL DISPLAY
if processedData != []:
    print("File read successfully.")
    print("------------------------------------")
    print("ORIGINAL DATA\n")
    for i, item in enumerate(original.items()):
        print(i + start, item) # i + start indexes the data by the line number in the file.
    print("------------------------------------")
    print("EVALUATION RESULTS\n")
    for i, item in enumerate(results.items()):
        print(i + start, item) # i + start indexes the data by the line number in the file.
    print()
else:
    print("Nothing to display\n")