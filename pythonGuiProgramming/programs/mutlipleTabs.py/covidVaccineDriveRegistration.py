"""
Details to enter
------------------------
PERSONAL INFO
- First name
- Last name
- DOB (calculated age must be 18 or above)
------------------------
CONTACT INFO
- Phone number (10 digits, non-zero 1st digit)
- E-mail address
    - Split string by '@' must result in 2 substrings
    - 1st substring must be more than 0 length
    - 1st substring must be alphanumeric
      (may have characters '.' and '_')
    - 2nd substring must contain
        - 1 domain name
        - 1 extension
        (separated by '.')
------------------------
LOCATION INFO
- PIN code (6 digits only)
- City (selection list ideally, but not feasible in time constraint)
- State (selection list ideally, but not feasible in time constraint)
========================
ORDER OF IMPORTANCE
1. CONTACT INFO (can help reveal personal & location details)
2. PERSONAL INFO (to identify user)
3. LOCATION INFO (to give appropriate vaccination locations)
"""
# INTERFACE
# Libraries and modules required
from alwaysImportMe import *

# Root frame for this...
cvdrRoot = Frame(tabControl)
# 
#========================
# LABELS
# Contact info labels
contactInfoLabels = [
    Label(cvdrRoot, text = "Phone"),
    Label(cvdrRoot, text = "E-mail")]
#------------------------
# Personal info labels
personalInfoLabels = [
    Label(cvdrRoot, text = "First name"),
    Label(cvdrRoot, text = "Last name"),
    Label(cvdrRoot, text = "DOB date"),
    Label(cvdrRoot, text = "DOB month"),
    Label(cvdrRoot, text = "DOB year")]
#------------------------
# Location info labels
locationInfoLabels = [
    Label(cvdrRoot, text = "PIN code"),
    Label(cvdrRoot, text = "City"),
    Label(cvdrRoot, text = "State")]
#========================
# INPUT BOXES
# Contact info inputs
contactInfoInputs = [
    Entry(cvdrRoot),
    Entry(cvdrRoot)]
#------------------------
# Personal info inputs
#____________
# DATE INPUTS
personalInfoInputs = [
    Entry(cvdrRoot),
    Entry(cvdrRoot),
    Spinbox(cvdrRoot, from_ = 1, to = 31, width = 6, wrap = True),
    Combobox(cvdrRoot, values = list(range(1, 13)), width = 6),
    Entry(cvdrRoot, width = 9)]
#------------------------
# Location info labels
locationInfoInputs = [
    Entry(cvdrRoot, text = "PIN code"),
    Entry(cvdrRoot, text = "City"),
    Entry(cvdrRoot, text = "State")]
#========================
# PACKING WIDGETS
# Contact info
Label(cvdrRoot, text = "CONTANT INFO", font = ("Helvetica Bold", 15)).pack()
for i in range(len(contactInfoLabels)):
    contactInfoLabels[i].pack()
    contactInfoInputs[i].pack()
#------------------------
# Personal info
Label(cvdrRoot, text = "PERSONAL INFO", font = ("Helvetica Bold", 15)).pack()
for i in range(len(personalInfoLabels)):
    personalInfoLabels[i].pack()
    personalInfoInputs[i].pack()
#------------------------
# Location info
Label(cvdrRoot, text = "LOCATION INFO", font = ("Helvetica Bold", 15)).pack()
for i in range(len(locationInfoLabels)):
    locationInfoLabels[i].pack()
    locationInfoInputs[i].pack()
#========================
# SUBMISSION
from re import *
from datetime import date
from tkinter import messagebox
# Contact info checks
def checkEmail():
    if search(r"[^\s]+@(gmail|yahoo|outlook).com$", contactInfoInputs[1].get()):
        return True
    return False
def checkPhone(): 
    if search(r"\d{10,11}", contactInfoInputs[0].get()):
        return True
    return False
# Personal info checks
def checkName():
    if search(r"[^\s]+", personalInfoInputs[0].get()):
        if search(r"[^\s]+", personalInfoInputs[1].get()):
            return True
    return False
def checkDate():
    try:
        d = int(personalInfoInputs[2].get())
        m = int(personalInfoInputs[3].get())
        y = int(personalInfoInputs[4].get())
    except: return False
    cur = date.today()
    age = cur.year - y
    if age < 18: return False
    elif age > 18: return True
    elif age == 18:
        if m < cur.month: return False
        elif m > cur.month: return True
        elif m == cur.month:
            if d < cur.date: return False
            else: return True
# Location info checks
def checkPin():
    if search(r"\d{6,7}", locationInfoInputs[0].get()):
        return True
    return False
def checkCityAndState():
    if search(r"[^\s]+", locationInfoInputs[1].get()):
        if search(r"[^\s]+", locationInfoInputs[2].get()):
            return True
    return False
# Total check
def check():
    print("Hello")
    errorList = []
    if not checkName():
        errorList.append("Name is invalid!")
    if not checkEmail():
        errorList.append("E-mails must only be from the following domains:\n- Google\n- Yahoo\n- Outlook.")
    if not checkPhone():
        errorList.append("Phone numbers must have 10 digits excluding code.")
    if not checkDate():
        errorList.append("Too young for the vaccination drive")
    if not checkPin():
        errorList.append("Invalid PIN code.")
    if not checkCityAndState():
        errorList.append("Invalid city and state.")
    if not errorList == []:
        errorMessage, i = "", 1
        for e in errorList:
            errorMessage = errorMessage + "\nERROR " + str(i) + "\n"
            errorMessage, i = errorMessage + e + "\n", i + 1
        messagebox.showerror("ATTENTION!", errorMessage)
    else: messagebox.showinfo("SUCCESS", "Registration successful")
# Submit button
Button(cvdrRoot, text = "SUBMIT", command = check).pack()