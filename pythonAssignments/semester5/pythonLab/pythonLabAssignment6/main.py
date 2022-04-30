from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
#========================
# MAIN WINDOW
w = Tk()
w.geometry("500x450")
w.title("1940223 - Pranav Gopalkrishna")
#========================
# PROGRESS BAR
p = Progressbar(w, length = 100, value = 0)
p.pack()
#========================
# MAIN
def appendInputSpace(e, ev, parent):
    if ev[0] == "s":
        v = ev[1:].split(",")
        e.append(Spinbox(parent, width = 3, from_ = int(v[0]), to = int(v[1])))
    elif ev[0] == "c":
        v = ev[1:].split(",")
        e.append(Combobox(parent, width = 3, values = v))
    elif ev[0] == "e":
        e.append(Entry(parent, width = 5))
questions = [
    "1+1=?",
    "2^3=?",
    "sqrt(25*4)=?",
    "1,1,3,5,8,?",
    "23,29,31,37,?"]
answers = [
    "2",
    "8",
    "10",
    "13",
    "41"]
# Creating display...
labels, entries, i = []*5, [], 0
entryValues = [
    "s0,10",
    "e",
    "e",
    "c11,13,15,12",
    "e"]
for q in questions:
    f = Frame(w)
    labels.append(Label(f, text = q, font = ("Sans Serif", 15)))
    appendInputSpace(entries, entryValues[i], f)
    # Packing...
    f.pack(fill = "x")
    labels[-1].pack(side = "left", padx = 50)
    entries[-1].pack(side = "right", padx = 50)
    i = i + 1
#========================
# BUTTON FOR CHECKING INPUTS
t = ScrolledText(w, width = 20, height = 6, font = ("Arial Italic", 15), bg = "light pink")
t.insert("1.0", "ANSWERS\n")
t["state"] = "disabled"
def checkAnswers():
    t["state"] = "normal"
    t.delete("1.0", "end")
    t.insert("1.0", "ANSWERS\n\n")
    i, val, max = 0, 0, len(answers)
    for i in range(0, max):
        ans = entries[i].get()
        if ans == answers[i]:
            val = val + 100 / max
        t.insert("end", questions[i] + ": " + ans + "\n")
    p.configure(value = val)
    """
    Alternatively, you can do...
    p["value"] = val
    """
    t["state"] = "disabled"
b = Button(w, text = "CHECK", command = checkAnswers)
# Packing stuff...
b.pack()
t.pack(pady = 30)
#========================
# BUTTON FOR PRINTING OUTPUTS
mainloop()