"""
Details to enter
- Name (not vital ifno)
- DOB
- Salary (monthly)
"""
# INTERFACE
# Libraries and modules required
from alwaysImportMe import *

# Root window...
leRoot = Frame(tabControl)
#========================
# LABELS
nameLabel = Label(leRoot, text = "Name")
dobLabels = [
    Label(leRoot, text = "DOB date"),
    Label(leRoot, text = "DOB month"),
    Label(leRoot, text = "DOB year")]
salaryLabel = Label(leRoot, text = "Salary")
#========================
# INPUTS
nameInput = Entry(leRoot, width = 20)
dobInputs = [
    Spinbox(leRoot, from_ = 1, to = 31, width = 6, wrap = True),
    Combobox(leRoot, values = list(range(1, 13)), width = 6),
    Entry(leRoot, width = 9)]
salaryInput = Entry(leRoot, width = 9)
#========================
# PACKING WIDGETS
nameLabel.pack()
nameInput.pack()

for i in range(len(dobLabels)):
    dobLabels[i].pack()
    dobInputs[i].pack()

salaryLabel.pack()
salaryInput.pack()
#========================
# SUBMISSION
from re import *
from datetime import date
from tkinter import messagebox
def getAge():
    try:
        d = int(dobInputs[0].get())
        m = int(dobInputs[1].get())
        y = int(dobInputs[2].get())
    except: return False
    cur = date.today()
    age = cur.year - y
    if m < cur.month: age = age - 1
    elif m == cur.month:
        if d < cur.date: age = age - 1
    return age
def loanAmt():
    age = getAge()
    try: salary = float(salaryInput.get())
    except: return -1
    a1, a2 = 0, 0
    if salary >= 50000: a1 = 300000
    elif salary >= 30000: a1 = 200000
    elif salary >= 15000: a1 = 100000

    if age >= 30: a2 = 100000
    elif age >= 25: a2 = 200000
    elif age >= 20: a2 = 300000

    if a1 == 0 or a2 == 0: return -1
    elif a1 < a2: return a1
    else: return a2
def showAmt():
    a = loanAmt()
    if a == -1:
        messagebox.showerror("NO LOAN AMOUNT", "You are not eligible for any loan amount.")
    else:
        messagebox.showinfo("LOAN AMOUNT", "You are eligible for a loan of {0}.".format(a))
Button(leRoot, text = "SUBMIT", command = showAmt).pack()