import tkinter
w = tkinter.Tk()
w.title("Button demo")
w.geometry("200x100")
# Label to reflect the action of the button...
l = tkinter.Label(w, text = "...")
l.grid(column = 0, row = 1)
# Function to be called by the button
def generalKenobi():
    if l.cget("text") == "...":
        """
        cget returns the value of the given attribute of the widget (here label).
        An aternative code for the same purpose is...
        if l["text"] == "..." etc.
        For more information, see tkWidgetObjectAnalysis.py...
        """
        l.configure(text = "General Kenobi!")
        """
        configure redefines one or more attributes of the given label.
        Alternatively, you can do...
        l["text"] = "General Kenobi!"
        For more information, see tkWidgetObjectAnalysis.py...
        """
    else:
        l.configure(text = "...")
"""
NOTES ON FUNCTION TO BE CALLED BY THE BUTTON
___
Since the function name should be defined in order for the button to call it,
and since Python is interpreted, the function should be defined before the button.
"""
# Button...
"""
Syntax:
Button(parent, text, font, command, etc.)
NOTE: All arguments are optional.
___
Function:
A widget that runs a specific function (given in the option command) when clicked.
"""
b = tkinter.Button(w, text = "Hello there!", command = generalKenobi)
# Note that the command option is optional, and may be None. In that case, the button would be a dummy.
b.grid(column = 0, row = 0)
# As with any widget including label, the grid position must be defined for it to show.
tkinter.mainloop()