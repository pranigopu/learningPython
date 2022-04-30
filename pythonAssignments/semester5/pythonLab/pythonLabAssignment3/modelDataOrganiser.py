# Write a program that separates the year, PC model and processor generation from a tuple, and store the data in a list.
# Expected I/P and O/P:
# I/P: (I7, 2019, Mac, Mac Pro, I5, 2015, I3, I5, I7, Lenovo Yoga, HP Envy, Dell XP, 2021,2020)
# O/P: {“Year”:[2015, 2019,2020,2021], “Processor”:[I3, I5, I7], “Model”:[ “Mac”, ”Mac Pro”, “Lenovo Yoga”, “HP Envy”, “Dell XP”]}
from datetime import date

# Removes extra whitespaces.
def trim(x):
    y, j = str(), x[0]
    for i in x:
        if not i.isspace(): y = y + i
        elif not j.isspace(): y = y + " "
        j = i
    return y[:-1] # Assumes that '\0' is appended in the function keyAndValue.

# Trims out beginning and spaces and brackets
def trimEnds(x):
    i = 0
    while x[i].isspace(): i = i + 1
    x, i = x[i:], 0
    while x[i].isspace(): i = i - 1
    if i < 0: x = x[:i]
    return x

# Checks whether the give year n is within b years from the current year
# (b years to the past or future)
def withinTimeBound(n, b):
    currentYear = date.today().year
    if n > currentYear - b and n < currentYear + b: return True
    return False

# Checks if an element is a processor generation, year or PC model
# Returns the appropriate key and value as a tuple
def keyAndValue(x):
    x, i, n = trimEnds(x) + "\0", 0, 0
    # x = x + "\0" is done so that end of string can be easily detected.
    # n can mean processor name or year, depending on what condition is met
    x, i = x[i:], 0
    # i was the 1st non-whitespace index.
    # Hence, x loses its initial whitespaces.
    # This will save some time trimming x, if it turns out to be a model name.
    if x[i] in ("i", "I"):
        # CONDITION 1: Checking if x is a processor generation
        i, n = i + 1, "I"
        while x[i].isnumeric(): i, n = i + 1, n + x[i]
        if x[i] == "\0" and n != "I": return ("Processor", n)
        # If n == "I", it means no number was found afterwards.
    else:
        # CONDITION 2: Checking of x is a valid year number (unabbreviated)
        while x[i].isnumeric(): i, n = i + 1, 10 * n + int(x[i])
        if x[i] == "\0" and withinTimeBound(n, 1000): return ("Year", n)
    # DEFAULT: Default to PC model
    return ("Model", trim(x))

def inputTuple(prompt):
    x = trimEnds(input(prompt))
    # Removing possible brackets...
    if x[0] == "(": x = x[1:]
    if x[-1] == ")": x = x[:-1]
    return tuple(x.split(","))

print("\nPC MODEL DATA ORGANISER\n")
inputData = inputTuple("Input tuple...\n")
outputData = {"Year":[], "Processor":[], "Model":[]}
for x in inputData:
    tmp = keyAndValue(x)
    outputData[tmp[0]].append(tmp[1])
print("\nOutput dictionary...")
print(outputData)
print()