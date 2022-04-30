import tkinter
w = tkinter.Tk()
w.title("Text widget demo")
w.geometry("350x500")
# Label for prompt...
l = tkinter.Label(w, text = "Enter text...", font = ("Helvetica Bold", 15))
l.grid(column = 0, row = 1)
# INPUTTING TEXT
# Text...
"""
Syntax:
Text(parent, width, height, etc.)
___
Function:
A widget to take multi-line user input.
Useful for applications such as messaging, notes, etc.
"""
t1 = tkinter.Text(w, width = 30, height = 10, bg = "light pink", font = ("Arial Italic", 15))
# The width option defines the max number of characters per line.
# The height option defined the max number of lines.
t1.grid(column = 0, row = 2)
# Function for reading the text...
def readText():
    print("========================")
    print("SUBMISSION")
    print("------------")
    print(t1.get("1.0", "end"))
    """
    For retrieving the input from a text box i.e. text widget, we use the get function with different arguments.
    The first argument is the point in the text from which you want start retrieving the input.
    The second argument is the point in the text until which you want to keep retrieving the input.
    Both arguments are strings.

    The first argument must be in the form "lineNumber.CharacterIndex", for example...
    "1.0", meaning line 1, character at index 0 (1st character).

    The second argument can be in the above form, or if you want to readd until the end of the input,
    you may give "end" or use the imported constant END (to be imported from tkinter.constants), which has the value "end".
    Note that using "end" or END will include a newline in your input. To avoid the inclusion of newline in the return value of get,
    you can do...
    t.get("1.0", "end")[:-1]
    
    Note that the starting point is inclusive, while the ending point is exclusive, meaning
    the character at the starting will be included, while the character at the ending point will be excluded.
    """
# Button to trigger reading of text...
b = tkinter.Button(w, text = "Submit", command = readText)
b.grid(column = 0, row = 3)
# READ-ONLY TEXT
t2 = tkinter.Text(w, width = 30, height = 10, bg = "light green", font = ("Helvetica Bold", 15))
t2.grid(column = 0, row = 0)
t2.insert("1.0", "Read only text!") # Inserts text into the text box.
"""
The insert method can be used for any text box (even text boxes with input).
It inserts a given string in the given position in the text.
As with the get function for text widgets, the positions are strings and can be given in the form...
"lineNumber.CharacterIndex", for example
"1.0", meaning line 1, character at index 0 (1st character).

You may also give literals such as "insert" and "end",
which can also be referred to by the imported constants INSERT and END (to be imported from tkinter.constants).
"""
t2.configure(state = "disabled") # Disables input
"""
Alternatively, you can do...
t2["state"] = "disabled"
"""
tkinter.mainloop()
"""
NOTES ON POSITIONS
___
Positions are always within available text.
If characters have not been entered beyond a certain position,
referring to positions beyond that point will simply default to the end position.
"""