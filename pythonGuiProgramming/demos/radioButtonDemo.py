import tkinter
w = tkinter.Tk()
w.title("Radio button demo")
w.geometry("300x200")
# Labels for prompt and output...
l1 = tkinter.Label(w, text = "Complete: ___, there are too many of them.")
l1.grid(column = 0, row = 0)

l2 = tkinter.Label(w)
l2.grid(column = 0, row = 5)
# Radio button...
"""
Syntax:
Radiobutton(parent, text, value, variable, etc.)
NOTE: All arguments are optional.
___
Function:
A widget that allows user selection.
This selection is such that only one radio button object in a window can be selected at a time.
"""
selectedOption = tkinter.IntVar() # Application variable for Tk objects.
"""
NOTES ON CONTROL VARIABLE...
We use IntVar because the values of the radio buttons are integers.
If the values were strings, we would use StringVar,
if the values were floating point values, we would use FloatVar, etc.
"""
r1 = tkinter.Radiobutton(w, text = "General Kenobi", value = 1, variable = selectedOption)
r2 = tkinter.Radiobutton(w, text = "Master Skywalker", value = 2, variable = selectedOption)
r3 = tkinter.Radiobutton(w, text = "Chancellor Palpatine", value = 3, variable = selectedOption)
r1.grid(column = 0, row = 1)
r2.grid(column = 0, row = 2)
r3.grid(column = 0, row = 3)
# Function for checking the selections...
def checkAnswer():
    print("Selected option:", selectedOption.get()) # Prints the selected radio button's value in the standard output console.
    if selectedOption.get() == 2:
        l2.configure(text = "Gooood!", font = ("Arial Italic", 15))
        """
        Alternatively, we could do...
        l2["text"] = "Gooood!"
        """
    else:
        l2.configure(text = "It's treason, then.", font = ("Helvetica Bold", 15))
# Button to trigger checking of selection...
b = tkinter.Button(w, text = "CHECK", command = checkAnswer)
b.grid(column = 0, row = 4)
tkinter.mainloop()