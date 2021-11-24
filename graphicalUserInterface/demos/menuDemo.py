import tkinter
w = tkinter.Tk()
w.title("Menu demo")
w.geometry("300x300")
# Some functions for demo purposes...
def q(): w.quit() # Ends the program.
def f11(): print("Option 1.1 selected.")
def f12(): print("Option 1.2 selected.")
def f21(): print("Option 2.1 selected.")
def f22(): print("Option 2.2 selected.")
#========================
# 1. Menu...
"""
Syntax:
Menu(parent, etc.)
NOTE: All arguments are optional.
___
Function:
A menu widget serves the purpose of a menu bar used in many applications.
It provides access to multiple operations in an organised and user-friendly manner.
The goal of this widget is to allow us to create all kinds of menus that can be used by our applications.
The core functionality provides ways to create three menu types: pop-up, toplevel and pull-down.
"""
# 1.1. Menu bar (which will contain options)...
m = tkinter.Menu(w)
# 1.2. Adding an executable command for the menu (as an option)...
m.add_command(label = "Quit", command = q)
"""
ISSUE
For some reason, this command is not showing.
It seems like commands are only accessible through sub-menus, and not the main menu directly...?
This is the case in my operating system at least (Mac OS).
"""
# 1.3. Adding sub-menus to the menu bar...
"""
Each menu bar option can be a menu itself (as we usually see in applications).
The root (or parent) of these option menus is the menu bar created previously.
"""
# Option 1 menu...
option1 = tkinter.Menu(m)
# Adding executable commands for the menu (as options within the option menu)...
m.add_cascade(label = "Option 1", menu = option1)
"""
add_cascade() creates a new hierarchical menu by linking a given menu to a parent menu.
Having linked the sub-menu to the main menu using this function,
any commands and items added to the sub-menu will be accessible as well.
"""
option1.add_command(label = "Option 1.1", command = f11)
option1.add_command(label = "Option 1.2", command = f12)
#------------
# Option 2 menu...
# Here, we will see how separators can be added between menu items.
option2 = tkinter.Menu(m)
m.add_cascade(label = "Option 2", menu = option2)
option2.add_command(label = "Option 2.1", command = f21)
option2.add_separator()
option2.add_command(label = "Option 2.2", command = f22)
#========================
# Assigning menu bar to "menu" option in root (or parent)...
"""
To make the menu bar visible and accessible by the user,
you need to assign this object to the "menu" option in the parent widget / window (also called root),
which in this case is w.
"""
w.configure(menu = m)
"""
Alternatively, you can do...
w["menu"] = m
"""
tkinter.mainloop()