import tkinter
w = tkinter.Tk()
w.title("Input demo")
w.geometry("500x300")
# Labels to reflect the outputs...
l0 = tkinter.Label(w, text = "Hello there!", font = ("Helvetica", 15))
l0.grid(column = 0, row = 0)

l1 = tkinter.Label(w)
l1.grid(column = 1, row = 1)

l2 = tkinter.Label(w)
l2.grid(column = 1, row = 2)
# Entry...
"""
Syntax:
Entry(parent, height, width, etc.)
NOTE: All arguments are optional.
___
Function:
A widget that stores user input.
"""
e = tkinter.Entry(w, width = 20)
# The width option defines the number of characters that are visible at a time.
e.grid(column = 1, row = 0)
# Function to be called by the button...
def checkAnswer():
    inputText = e.get()
    # Here, the get function returns the text entered by the user in the space provided by the Entry widget.
    #------------------------
    # Extra code to add "..." to the first 20 characters in the input text exceeds 20 characters...
    try:
        inputText[19]
        inputText = inputText[:20] + "..."
    except: pass
    #------------------------
    l1.configure(text = "Your answer was \"" + inputText + "\"", font = ("Arial Italic", 15))
    if inputText.lower() == "general kenobi!":
        l2.configure(text = "Gooood", font = ("Arial Italic", 15))
    else:
        l2.configure(text = "WRONG ANSWER", font = ("Helvetica Bold", 15))
b = tkinter.Button(w, text = "CHECK", command = checkAnswer)
b.grid(column = 2, row = 0)
tkinter.mainloop()