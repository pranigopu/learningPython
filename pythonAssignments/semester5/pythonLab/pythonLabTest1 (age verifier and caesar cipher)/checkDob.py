from datetime import date
import re
def checkDate(d):
    x = d.split("-")
    try:
        dd, mm, yyyy = int(x[0]), int(x[1]), int(x[2])
        dob = date(yyyy, mm, dd)
        return dob
    except: return False
def votingEligibility(dob):
    dob = checkDate(dob)
    if not dob: return -1 # If the DOB is not in correct format.
    cur = date.today() # Current date
    # The following code ensures that the person's 18th birthday is today or has passed...
    yearDifference = cur.year - dob.year
    monthDifference = cur.month - dob.month
    dayDifference = cur.day - dob.day
    if yearDifference > 18: return 1 # Person is 19 or above.
    elif yearDifference == 18 and monthDifference > 0: return 1 # Today's month is after birthday month.
    elif yearDifference == 18 and monthDifference == 0 and dayDifference >= 0: return 1 # Today's day is birthday or after birthday (in the birthday month).
    return 0
print("\nDate format: dd-mm-yyyy")
dob = input("Enter DOB: ")
check = votingEligibility(dob)
if check == -1: raise Exception("Wrong date format!")
elif check == 0: raise Exception("Too young to vote!")
else: print("You are eligible to vote.")