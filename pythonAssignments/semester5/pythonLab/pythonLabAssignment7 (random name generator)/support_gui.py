from tkinter import *
def getDim(s):
    lines = s.split("\n")
    width = max(list(map(len, lines)))
    height = len(lines)
    return (width, height)
def updateTextBox(t, s, flex, start, end):
# t => text box widget
# s => string to be inserted
# flex => flexible dimensions, based on the string
    if flex: (t["width"], t["height"]) = getDim(s)
    t["state"] = "normal"
    t.delete(start, end)
    t.insert(start, s)
    t["state"] = "disabled"
def utb_simple(t, s): updateTextBox(t, s, False, "1.0", "end")
def utb_flex(t, s): updateTextBox(t, s, True, "1.0", "end")
def utb_header(t, s): updateTextBox(t, s, False, "2.0", "end")