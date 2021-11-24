import tkinter
from tkinter import messagebox # Module for creating and handling message boxes.
w = tkinter.Tk()
w.title("Message box demo")
w.geometry("500x500")
# 1. Welcome message box :)
messagebox.showinfo("Hello there!", "Welcome, user :)")
# Label for information...
tkinter.Label(w, text = "Showing all the available options...").pack() # As you can see, no need to assign a variable and then pack it, for it to display.
# 2. Seeing different types of message boxes...
# Functions...
# This is for demo purposes; it is not necessary to use functions for message boxes...
def showInfo(): messagebox.showinfo("Info", "Letting you know ;)")
def showWarning(): messagebox.showwarning("Warning", "Beware :O")
def showError(): messagebox.showerror("Error", "Something awry :(")

def askOkCancel(): messagebox.askokcancel("Okay or cancel?", "Shall we proceed?")
def askYesNo(): messagebox.askyesno("Yes or no?", "Agreed?")
def askYesNoCancel(): messagebox.askyesnocancel("Yes, no or cancel?", "Will you marry me?")
def askRetryCancel(): messagebox.askretrycancel("Retry or cancel?", "What to do?")
def askQuestion(): messagebox.askquestion("Question", "1 + 1 = ?")
#------------
# Buttons to trigger the above functions...
tkinter.Button(w, text = "showinfo", command = showInfo).pack()
tkinter.Button(w, text = "showwarning", command = showWarning).pack()
tkinter.Button(w, text = "showinfo", command = showError).pack()

tkinter.Button(w, text = "askokcancel", command = askOkCancel).pack()
tkinter.Button(w, text = "askyesno", command = askYesNo).pack()
tkinter.Button(w, text = "askyesnocancel", command = askYesNoCancel).pack()
tkinter.Button(w, text = "askretrycancel", command = askRetryCancel).pack()
tkinter.Button(w, text = "askquestion", command = askQuestion).pack()
# 4. Seeing the return of the interactive message box functions...
# Label for information...
tkinter.Label(w, text = "Seeing the return of the interactive message box functions...").pack()
#------------
# Functions...
def askOkCancelAnswer(): print(messagebox.askokcancel("Okay or cancel?", "Shall we proceed?"))
def askYesNoAnswer(): print(messagebox.askyesno("Yes or no?", "Agreed?"))
def askYesNoCancelAnswer(): print(messagebox.askyesnocancel("Yes, no or cancel?", "Will you marry me?"))
def askRetryCancelAnswer(): print(messagebox.askretrycancel("Retry or cancel?", "What to do?"))
def askQuestionAnswer(): print(messagebox.askquestion("Question", "1 + 1 = ?"))
#------------
# Buttons to trigger the above functions...
tkinter.Button(w, text = "askokcancel", command = askOkCancelAnswer).pack()
tkinter.Button(w, text = "askyesno", command = askYesNoAnswer).pack()
tkinter.Button(w, text = "askyesnocancel", command = askYesNoCancelAnswer).pack()
tkinter.Button(w, text = "askretrycancel", command = askRetryCancelAnswer).pack()
tkinter.Button(w, text = "askquestion", command = askQuestionAnswer).pack()
#========================
tkinter.mainloop()