# Create a list and store the details employees (ID number, name, mobile number).
# Name of a person is in the form first name space and then last name (Ex: Gautam Menon).
# Check the validity of the name entered and validity of the mobile number.
# A valid mobile number must consist of 10 digits and the first digit must not be zero.
# Print 'Invalid input ‘when conditions are not satisfied and break the process of getting input. Display the results (stored values) in a list.
# Note: Separate lists for ID, name, mobile number.

def nameInput(prompt):
    name = input(prompt) + "*"
    nameParts = []  # Stores each part of the name separated by spaces
    i = 0           # Iterating variable
    checkpoint = 0  # Marks the lower bound to slice the original name string
    while name[i] != "*":
        while name[i].isspace(): i = i + 1
        checkpoint = i
        if name[i].isalpha():
            while name[i].isalpha(): i = i + 1
        else:
            break
        nameParts.append(name[checkpoint:i])
    if name[i] == "*" and len(nameParts) == 2:
        return nameParts[0] + " " + nameParts[1]
    return "*"
    # Note:
    # Since the len function is so readily available, I used it here.
    # Alternatively, I could count the number of iterations to keep count of the number of name parts.

def mobileNumberInput(prompt):
    mobileNumber = input(prompt) + "*"
    i = 0
    digitCount = 0
    finalMobileNumber = str()
    while digitCount < 10 and mobileNumber[i] != "*":
        while mobileNumber[i].isspace(): i = i + 1
        if mobileNumber[i].isnumeric():
            while mobileNumber[i].isnumeric() and digitCount < 10:
                finalMobileNumber = finalMobileNumber + mobileNumber[i]
                digitCount = digitCount + 1
                i = i + 1
                # i = i + 1 must be at the end, so that you can immediately check the entry condition for the increased i value.
        elif mobileNumber[i] != "*":
            digitCount = 11
    if digitCount == 10 and finalMobileNumber[0] != "0":
        return finalMobileNumber
    return "*"

# ALTERNATE, SIMPLER MOBILE NUMBER INPUT THAT DOESN'T CHECK FOR EXTRA SPACES
# def mobileNumberInput(prompt):
#    mobileNumber = input(prompt) + "*"
#    i = 0
#    digitCount = 0
#    finalMobileNumber = str()
#    while mobileNumber[i].isnumeric() and digitCount < 10:
#        finalMobileNumber = finalMobileNumber + mobileNumber[i]
#        digitCount = digitCount + 1
#        i = i + 1 # Must be at the end, so that you can immediately check the entry condition for the increased i value.
#    if digitCount == 10 and finalMobileNumber[0] != "0":
#        return finalMobileNumber
#    return "*"

i = 0

# STORAGE LISTS
ids = []
names = []
mobileNumbers = []

# INFORMATION
print("\nEMPLOYEE LIST CREATION PROGRAM")
print("Enter names and mobile numbers of employees.")
print("Name must have only a distinct first and last name, with no special characters.")
print("Mobile number must be 10 digits, and first digit must not be 0.")
print("Enter in a wrong input format to end input process.")

# INPUT LOOP
while i < 100:
    i = i + 1
    print("\nENTER EMPLOYEE", i, "DETAILS")
    name = nameInput("Name\t: ")
    if name == "*":
        break
    mobileNumber = mobileNumberInput("Mobile\t: ")
    if mobileNumber == "*":
        break
    ids.append(i)
    names.append(name)
    mobileNumbers.append(mobileNumber)
print("Invalid input!") # The loop only ends with a wrong input :)

# DISPLAY OF DATA
print("------------------------------")
if len(ids) > 0:
    print("EMPLOYEE LIST DISPLAY")
    for i in ids:
        print("\nID:", i)
        print("Name\t: " + names[i - 1])
        print("Mobile\t: " + mobileNumbers[i - 1])
else:
    print("Nothing to display!\n")