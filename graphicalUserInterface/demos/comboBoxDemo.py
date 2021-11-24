import tkinter
from tkinter import ttk # See ttkNotes.txt
w = tkinter.Tk()
w.title("Combobox demo")
w.geometry("300x200")
# Labels for prompt and output...
l1 = tkinter.Label(w, text = "Pick the right answer for \"Hello there!\"")
l1.grid(column = 0, row = 0)

l2 = tkinter.Label(w)
l2.grid(column = 0, row = 3)
# Combobox...
"""
Syntax:
Combobox(parent, values, etc.)
NOTE: All arguments are optional.
___
Function:
Combobox is a combination of Listbox and an entry field.
It contains a down arrow to select from a list of options.
It helps the users to select according to the list of options displayed.
"""
c = ttk.Combobox(w)
c.configure(values = ("General Kenobi", "Master Skywalker", "Admiral Tarkin", "Chancellor Palpatine"))
"""
Alternatively, you can do...
c["values"] = ("General Kenobi", "Master Skywalker", "Admiral Tarkin", "Chancellor Palpatine")
"""
c.current(1) # Intended default value (the corresponding index is passed).
c.grid(column = 0, row = 1)
# Selection check function...
def checkAnswer():
    if c.get() == "General Kenobi":
        l2.configure(text = "Gooood!", font = ("Arial Italic", 15))
    else:
        l2.configure(text = "It's treason then.", font = ("Helvetica Bold", 15))
# Button for triggerring selection check...
b = tkinter.Button(w, text = "CHECK", command = checkAnswer)
b.grid(column = 0, row = 2)
tkinter.mainloop()