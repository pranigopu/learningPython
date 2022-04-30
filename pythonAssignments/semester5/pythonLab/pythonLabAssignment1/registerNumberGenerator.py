# Write a program that asks the user for this three information (Year, Program, Enrollment number) and generate their Register No.
# Example...
# Year = 2018
# Program = BSC
# Enrollment number = 3265
# Output = 18BSC3265
from datetime import date
def inputNumericString(promptMessage, errorMessage):
    while True:
        n = input(promptMessage)
        if n.isnumeric():
            return n
        else:
            print(errorMessage)

def inputYear(promptMessage, errorMessage):
    # Extracting the attribute "year" from a data object...
    currentYear = date.today().year
    while True:
        year = inputNumericString(promptMessage, errorMessage)
        if int(year) >= currentYear - 1000 and int(year) <= currentYear + 1000:
            return year
        print(errorMessage)

def processProgramName(program):
    processedProgramName = str()
    allowedCharacters = (".", " ", "\t")
    for i in program:
        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
            processedProgramName = processedProgramName + i.upper()
        elif i not in allowedCharacters:
            processedProgramName = "*"
            break
    return processedProgramName

def inputProgramName(promptMessage, errorMessage):
    while True:
        programName = input(promptMessage)
        programName = processProgramName(programName)
        if programName != "*" and len(programName) > 1:
            return programName
        print(errorMessage)

print("\nREGISTER NUMBER GENERATOR\n")
print("Enter your details...\n")
year = inputYear("Year of admission: ", "Invalid year entry!")
programName = inputProgramName("Selected program: ", "Invalid program name!")
enrollmentNumber = inputNumericString("Enrollment number: ", "Invalid enrollment number!")

registerNumber = year[-2] + year[-1] + programName + enrollmentNumber
print("Generated register number: " + registerNumber + "\n")