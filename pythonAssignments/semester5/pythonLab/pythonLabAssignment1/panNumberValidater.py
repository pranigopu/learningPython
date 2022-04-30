# Write a Python program to store Pan number of each employee and check whether the pan is valid or not.
# The PAN is a ten-character long alpha-numeric unique identifier.
# The first five characters are letters (in uppercase by default), followed by four numerals, and the last (tenth) character is a letter.
print()
while True:    
    pan = input("Enter your PAN for format validation: ")
    if len(pan) == 10:
        break
    print("PAN number must be 10 characters long!")
    
# Note that the upper bound is not included in a slice
part1 = pan[0:4].upper()
part2 = pan[4].upper()
part3 = pan[5:9]
part4 = pan[9].upper()

# ERROR CHECKING
errorList = []
holderTypes = ("A", "B", "C", "F", "G", "H", "L", "J", "P", "T")
for i in part1:
    if i < "A" or i > "Z":
        errorList.append("1st 4 characters must be letters.")
        break
if part2 not in holderTypes:
    errorList.append("Unrecognised holder type denoted by 5th character.")
if not part3.isnumeric():
    errorList.append("Characters 6 to 9 must be numeric.")
if part4 < "A" or part4 > "Z":
    errorList.append("Last character must be a letter.")

print()
pan = part1 + part2 + part3 + part4
if len(errorList) == 0:
    print("Your PAN, " + pan + ", is in valid format.")
else:
    print("Your PAN has the following issues:")
    for i in errorList:
        print("- " + i)
print()