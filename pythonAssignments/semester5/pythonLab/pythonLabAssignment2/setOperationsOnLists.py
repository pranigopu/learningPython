# Take two lists, and write a python program (separate functions for each operation) that returns a list that contains only
# • Elements two sets have in common. (Intersection)
# • All the elements from both sets. (Union)
# • Elements present on one set, but not on the other. (Difference)
# • Elements from both sets, that are not present on the other. (Symmetric difference)

# Make sure your program works on two lists of different sizes.

def union(list1, list2):
    # return list(set(list1 + list2)) # Slightly cheaty code
    combined = list1 + list2
    result = []
    for i in combined:
        if i not in result:
            result.append(i)
    return result

def intersection(list1, list2):
    # return list(set(list1).intersection(set(list2))) # Slightly cheaty code
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result

def difference(list1, list2):
    # return list(set(list1).difference(set(list2))) # Slightly cheaty code
    result = []
    for i in list1:
        if i not in list2 and i not in result:
            result.append(i)
    return result

def symmetricDifference(list1, list2):
    # return list(set(list1).symmetric_difference(set(list2))) # Slightly cheaty code
    return union(difference(list1, list2), difference(list2, list1))

a = [1, 4, 2, 5, 4, 2, 6]
b = [5, 6, 2, 5, 4, 3]
c = [4, 5, 5, 8, 0, 45, 66, 73, 223]
d = [6, 7, 88, 45, 66, 23, 62, 22]
result = []
nameToListMap = {"a" : a, "b": b, "c" : c, "d" : d}
yesOptions = ["y", "yea", "yes", "yeah"]

def operate():
    result = []
    try:
        list1 = nameToListMap[input("\nList 1: ")]
        print("=", list1)
        list2 = nameToListMap[input("List 2: ")]
        print("=", list2)
    except:
        print("Unavailable list!")
        return []
    operation = input("Operation: ")
    if operation.lower() == "u": result = union(list1, list2)
    elif operation.lower() == "i": result = intersection(list1, list2)
    elif operation.lower() == "d": result = difference(list1, list2)
    elif operation.lower() == "s": result = symmetricDifference(list1, list2)
    else: print("Invalid operation!")
    return result

def viewLists():
    print()
    for i in nameToListMap.keys():
        print(i, "=", nameToListMap[i])

def viewOperations():
    print("\nu : Union")
    print("i : Intersection")
    print("d : Difference")
    print("s : Symmetric difference")

print("\nSET OPERATIONS ON LISTS", end = "")
while True:
    print("\n------------------------")
    print("1. Operate on lists")
    print("2. View lists")
    print("3. View operations")
    print("x. Exit")
    option = input("Enter option... ")

    if option == "1": print("Result:", operate())
    elif option == "2": viewLists()
    elif option == "3": viewOperations()
    elif option == "x": break
    else: print("Invalid option!")
    
    option = input("\nEncore? ")
    if option.lower() not in yesOptions: break
print("Program ended.\n")