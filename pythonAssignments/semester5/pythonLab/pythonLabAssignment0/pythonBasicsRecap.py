print("OPTIONS")
print("1. Name and register number")
print("2. Consecutive integer adder")
response = input("Enter option: ")
if response == "1":
    print("--------")
    string = []
    string.append("Pranav")
    string.append("Gopalkrishna")
    string.append("1940223")
    # Doing string += "Pranav" will result in
    # each character of the string being added to the list
    # as a separate element.
    combined = str()
    # str() is a built-in function used to initialise a string object.
    # Hence, it is a constructor for the string class.
    # Giving no argument in the function returns an emty string.
    for i in range(0, 3):
        combined += string[i] + " "
    print(combined)
elif response == "2":
    print("--------")
    try:
        num1 = int(input("Enter lower limit integer: "))
        num2 = int(input("Enter upper limit integer: "))
        sum = int()
        # int() is a built-in function to
        #   - initialise an integer
        #   - convert a floating point number or string to an integer, if possible
        # Giving no argument returns 0.
        for i in range(num1, num2 + 1):
            sum += i
        print("The sum of integers from the lower to upper limit is", end = " ")
        print(sum)
    except:
        print("Invalid inputs!")