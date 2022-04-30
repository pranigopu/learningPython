# Perform the following operations with List datatype:
# Create a list called x of values 10, 20, 30, 45, 50 and also reverse the list.
# Create a list called y of string names of students Bob, Alex, Jim, Jane, and Smith. Then append a new name Jack to the list and print the entire list.
# Add a student name Cheryl to the front of the list y and print the entire list.
# Rename Alex to Catalin in list y and print the entire list.

x = [10, 20, 30, 45, 50]
y = ["Bob", "Alex", "Jim", "Jane", "Smith"]

print("\n========================\nLIST PART\n------------\n")

print("My lists...")
print("x = ", end = " ")
print(x)
print("y = ", end = " ")
print(y)

print("\nReversing list x...")
print(x[::-1])

print("\n......\nNow working with list y...")
y.append("Jack")
print("\nAfter appending...")
print(y)

y.insert(0, "Cheryl")
print("\nAfter inserting to the front...")
print(y)

max = len(y)
for i in range(0, max):
    if y[i] == "Alex":
        y[i] = "Catalin"
        break
print("\nAfter replacing item...")
print(y)

# And also perform the slicing and striding operations with index concept with strings.
# Upload the screenshots of the above-said operations as a single pdf or word file here. 

print("\n========================\nSTRING SLICING AND STRIDING PART\n------------\n")
print("(Indices start from 1 here, and the limits are inclusive)")
yesOptions = ["yes", "Yes", "YES", "y", "Y", "yea", "Yea"]
while True:
    try:
        myString = input("\nEnter thy string: ")

        print("Character to index mapping...")
        max = len(myString)
        for i in range(0, max):
            print(myString[i], end = "\t: ")
            print(i + 1)
        startIndex = int(input("\nSlice string from: ")) - 1
        endIndex = int(input("Slice string until: "))
        stride = int(input("Enter stride value: "))
        
        print("Thy result...")
        print(myString[startIndex:endIndex:stride])
        # Generally, endIndex is the exclusive upper bound, i.e. the character with index endIndex is not selected.
        # Here, we have designed it so that the character at the endIndex position(visually, not actually) is included as well.
        
        option = input("\nEncore? ")
        if option in yesOptions:
            print("Encore, then!")
        else:
            print("'Tis done, then.")
            break
    except:
        print("Hast thou entered wrongly, perchance?")
        break