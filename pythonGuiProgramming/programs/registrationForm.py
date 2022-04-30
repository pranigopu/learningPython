from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
# ScrolledText in based on Text, and mainly differs in appearance and user experience.
from tkinter.messagebox import showerror
from re import *
lp = 20 # Left padding
yt = 40 # y-tick i.e. change in y to allow for character height and some spacing.
gap = lp + 50 # Space to account for labels and left padding
# Root window...
root = Tk()
root.title("Bloodbath Registration")
root.geometry("800x300")

# Labels...
Label(root, text = "Name").place(x = lp, y = yt)
Label(root, text = "DOB").place(x = lp, y = yt*2)
Label(root, text = "E-mail").place(x = lp, y = yt*3)
Label(root, text = "Phone").place(x = lp, y = yt*4)

# Entries...
#------------
# Name...
titles= ("Mrs.", "Ms.", "Mr.", "Dr.")
title = Combobox(root, values = titles, state = "readonly", width = 4)
title.place(x = gap, y = yt)
title.current(1) # Index of the current (default) value that the combobox widget's input is set to.

name = Entry(root, width = 20)
name.place(x = gap + 64, y = yt)
#------------
# Date...
months = []
for i in range(1, 10): months.append("0" + str(i))
for i in range(10, 13): months.append(str(i))
# A date related validation function...
def getMaxDay(m):
    if int(m) in (1, 3, 5, 7, 8, 10, 12): return 31
    elif int(m) == 2: return 29
    else: return 30
mm = Combobox(root, values = months, state = "readonly", width = 4)
mm.place(x = gap, y = yt*2)
mm.current(2) # Index of the current (default) value that the combobox widget's input is set to.

dd = Spinbox(root, from_ = 1, to = 31, width = 2, wrap = True)
dd.place(x = gap + 64, y = yt*2)

yyyy = Spinbox(root, from_ = 1985, to = 2000, width = 4, wrap = True)
yyyy.place(x = gap + 64 + 47, y = yt*2)
#------------
# E-mail
email = Entry(root, width = 27)
email.place(x = gap, y = yt*3)
#------------
# Phone...
defaultCode = StringVar() # To help set default value.
defaultCode.set("91") # Setting default value
countryCode = Spinbox(root, from_ = 0, to = 10000000, width = 8, wrap = True, textvariable = defaultCode)
countryCode.place(x = gap, y = yt*4)

phone = Entry(root, width = 16)
phone.place(x = gap + 100, y = yt*4)
#------------
# Text box
text = ScrolledText(root, width = 50, height = 13, font = ("Arial", 14), borderwidth = 10, wrap = "word")
text.place(x = gap + 275, y = yt)
text.insert("1.0", "Registration information:\n")
text["state"] = "disabled"
#------------
# Submission...
def checkEmail():
    if search(r"[^\s]+@(gmail|yahoo|outlook).com$", email.get()):
        return True
    return False
def checkPhone(): 
    if countryCode.get() == "91" and search(r"\d{10,11}", phone.get()):
        return True
    return False
def checkDate():
    try:
        m = int(mm.get())
        d = int(dd.get())
        y = int(yyyy.get())
    except: return False
    if d < 1 or d > getMaxDay(m): return False
    if y < 1985: return False
    elif y == 1985 and m < 3: return False
    elif y > 2000: return False
    elif y == 2000 and m > 3: return False
    return True
def checkName():
    if search(r"[^\s]+", name.get()): return True
    return False
def createText():
    text["state"] = "normal"
    text.delete("1.0", "end")
    text.insert("1.0", "Registration information:\n")
    dob = dd.get() + "-" + mm.get() + "-" + yyyy.get()[-2:]
    regNo = dd.get() + mm.get() + yyyy.get()[-2:] + "-" + phone.get()[-4:]
    # The message...
    textMessage = """
========================
Hi {} {}, thank you for your interest and registration.
------------
You are successfully registered for Bloodbath event.
------------
We used \n- your DOB {}\n- your phone number {}\nto generate your registration ID, {}.
------------
Soon event details will be shared through your e-mail:\n{}.
    """.format(title.get(), name.get(), dob, phone.get(), regNo, email.get().lower())
    text.insert("insert", textMessage)
    text["state"] = "disabled"
def check():
    errorList = []
    if not checkName():
        errorList.append("Name is missing!")
    if not checkEmail():
        errorList.append("E-mails must only be from the following domains:\n- Google\n- Yahoo\n- Outlook.")
    if not checkPhone():
        errorList.append("Phone numbers must be from India (+91) and have 10 digits excluding code.")
    if not checkDate():
        errorList.append("Enter an appropriate date not before March 1985, and not after March 2000.")
    if not errorList == []:
        errorMessage, i = "", 1
        for e in errorList:
            errorMessage = errorMessage + "\nERROR " + str(i) + "\n"
            errorMessage, i = errorMessage + e + "\n", i + 1
        showerror("ERRORS FOUND!", errorMessage)
    else: createText()
submit = Button(root, text = "Submit", command = check)
submit.place(x = gap*2, y = yt*5)
#------------
mainloop()