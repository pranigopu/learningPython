import tkinter
w = tkinter.Tk()
w.title("Spinbox demo")
w.geometry("350x500")
# Spinbox...
"""
Syntax:
Spinbox(parent, from_, to, width, wrap, command, etc.)
NOTE: All arguments are optional.
('from_' is used because 'from' is already a keyword in Python)
('wrap' ensures that if you reach a bound value and click further in the same direction, the value will go to the opposite bound)
___
Function:
The Spinbox widget is an alternative to the Entry widget or even the Combobox widget.
It provides a range of values to the user, out of which the user can select any one value.
The user may also input directly, as in an Entry widget.
Another difference from Entry widgets is that a Spinbox widget can trigger commands (functions / methods) like a button.
The trigger is done using the up/down arrow buttons on the side of the Spinbox widget.
"""
# Floating point value range...
s1 = tkinter.Spinbox(w, from_ = 1, to = 10, width = 10, wrap = True)
s1.grid(column = 0, row = 0)

# Discrete value range...
"""
Here, you can have any set of values that you want to give as options in the spin box.
This allows selection of discrete values of any kind.
"""
x = ("Hey", 2.3, 2, "Bye", 3.14, "I am Boar")
s2 = tkinter.Spinbox(w, values = x, width = 10, wrap = True)
s2.grid(column = 0, row = 1)

tkinter.mainloop()