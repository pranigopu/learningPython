from support_gui import *
from support_nongui import *
from tkinter.ttk import Combobox
#========================
# MAIN WINDOW
w = Tk()
w.geometry("500x450")
w.title("1940223 - Pranav Gopalkrishna")
#========================
# FRAMES
frames = [
    Frame(w, pady = 20),
    Frame(w, padx = 20, pady = 20),
    Frame(w, padx = 20, pady = 20)]
# Packing frames...
for f in frames: f.pack(side = "top")
#========================
# INPUT COMBO BOX
promptLabel = Label(frames[0], text = "Starting alphabet", font = ("Arial", 15))
inp = Combobox(frames[0], values = alphabetList(), width = 2)
#========================
# RANDOM NAME GENERATION
# Random name generating function and trigger button...
display = Text(
    frames[1],
    height = 1,
    font = ("Arial", 15),
    state = "disabled",
    borderwidth = 2,
    relief = "ridge",
    padx = 10,
    pady = 10)
def displayRandomName():
    c = inp.get()
    if c.isalpha(): utb_flex(display, "A random name from \"" + c + "\" is " + getRandomName(c) + ".")
    else: utb_flex(display, "Input alphabets only!")
utb_flex(display, "Generated name will be displayed here.") # Initial default text.
generateButton = Button(frames[0], text = "GENERATE", command = displayRandomName)
#========================
# TEXT BOXES
texts, fa = [], ("M", "P", "Q") # fa => featured alphabets
for x in fa:
    t = Text(
            frames[2],
            width = 14,
            height = 12,
            font = ("Arial", 15),
            borderwidth = 2,
            relief = "ridge",
            padx = 10,
            pady = 10)
    utb_simple(t, "Starting from " + x + "...")
    texts.append(t)
for i in range(0, len(texts)): utb_header(texts[i], "\n\n" + getTopNames(fa[i], 10))
#========================
# PACKING WIDGETS FOR EACH FRAME
#------------------------
# FRAME 1
promptLabel.grid(column = 0, row = 0, padx = 5)
inp.grid(column = 1, row = 0, padx = 5)
generateButton.grid(column = 2, row = 0, padx = 5)
#------------------------
# FRAME 2
display.pack(side = "left", expand = True)
#------------------------
# FRAME 3
for t in texts: t.pack(side = "left", fill = "both", expand = True)
#========================
mainloop()