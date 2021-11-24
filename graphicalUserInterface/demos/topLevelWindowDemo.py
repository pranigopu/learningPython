import tkinter
# Root window...
root = tkinter.Tk()
root.title("Root window")
root.geometry("200x200")

# Top-level window...
"""
Syntax:
TopLevel(options...)
NOTE: All arguments are optional.
___
Function:
It creates a separate window, apart form the root, that can be a parent to one or more widgets.
They are termed as "top-level" because they are not children of any other objects. However, unlike the root,
closing a top-level window won't stop the program (application).
There can be multiple such windows created in a single program (or application), either at the start, or dynamically.
Note that if the root window is closed, all top-level windows close,
since the root window has final control over the program's execution.
"""
top = tkinter.Toplevel()
top.title("Top-level window")
top.geometry("200x200")
# More top-level windows created dynamically...
# Function to create top-level window...
def newWindow():
    top = tkinter.Toplevel()
    top.title("New window")
    top.geometry("200x200")
# Button to trigger the above function...
tkinter.Button(root, text = "New Window", command = newWindow).pack()
tkinter.mainloop()