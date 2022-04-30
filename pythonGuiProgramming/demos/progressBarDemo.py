import tkinter
from tkinter import ttk
w = tkinter.Tk()
w.title("Progressbar demo")
w.geometry("350x200")
# Label for progressbar...
l = tkinter.Label(w, text = "Progress", font = ("Helvetica Bold", 15))
l.grid(sticky = "e", column = 0, row = 0)
# Progressbar...
"""
Syntax:
Progressbar(parent, length, value, etc.)
(length defines the total length of the bar)
(value defines the length of the bar that is covered)
NOTE: All arguments are optional.
___
Function:
A widget that allows user selection.
This selection is such that only one radio button object in a window can be selected at a time.
"""
p = ttk.Progressbar(w, length = 100, value = 0)
p.grid(sticky = "e", column = 1, row = 0)
# Some code to show change in progress bar...
#------------------------
questions = ["1+1=?", "2^3=?", "sqrt(25*4)=?", "1,1,3,5,8,?", "23,29,31,37,?"]
answers = ["2", "8", "10", "13", "41"]
# Creating display...
labels, entries, i = [], [], 1
for q in questions:
    labels.append(tkinter.Label(w, text = q, font = ("Sans Serif", 15)))
    entries.append(tkinter.Entry(w, width = 5))
    # Grid placement...
    labels[-1].grid(sticky = "e", column = 0, row = i)
    entries[-1].grid(column = 1, row = i)
    i = i + 1
# Answer checking function...
# (The more answers you correctly give, the more the progress bar fills)
def checkAnswers():
    i, val, max = 0, 0, len(answers)
    for i in range(0, max):
        if entries[i].get() == answers[i]:
            val = val + 100 / max
    p.configure(value = val)
    """
    Alternatively, you can do...
    p["value"] = val
    """
# Button for triggering answer checking...
b = tkinter.Button(w, text = "CHECK", command = checkAnswers)
b.grid()
#------------------------
tkinter.mainloop()