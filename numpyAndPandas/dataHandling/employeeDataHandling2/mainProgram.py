from functionDefinitions import *
questions = """
QUESTIONS
1. Find the missing values and give a report of it.
2. Fetch all the rows having Salary >80000
3. Fetch all the rows having Team = Legal and Finance
4. Find the missing values in Senior Management and replace it with NONE
5. Find the employees of having Bonus % more than 12 and reduce it with 2."""
map = {
# Format: Question number: (Function name, Arguments)
    '?': (print, [questions]),
    '1': (report_missingValues, []),
    '2': (report_rowsAboveSalaryAmount, [8000]),
    '3': (report_rowsWithGivenTeamNames, [['Legal', 'Finance']]),
    '4': (report_replaceMissingValues, ["Senior Management", "NONE"]),
    '5': (report_reduceBonus, [12, 2]),
}
print("\nASSIGNMENT 9 - PYTHON LAB")
while True:
    print("\n" + "="*24)
    print("MAIN LOOP")
    print("(Enter a hyphen '-' to exit)")
    print("(Enter a question mark '?' to see questions)")
    print("_"*24)
    option = input("Input question number: ")
    print("\n" + "="*24)
    try:
        if option == '-':
            print("\nGoodbye!\n")
            break
        map[option][0](*map[option][1])
    except: print("Invalid option!")